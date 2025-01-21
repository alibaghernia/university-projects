from skfuzzy import control as ctrl
import skfuzzy as fuzz
import numpy as np

# تعریف متغیرهای فازی
room_temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'room_temperature')
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')
mode = ctrl.Consequent(np.arange(0, 3, 1), 'mode')  # 0: Cooling, 1: Heating, 2: Fan Only

# تعریف توابع عضویت برای دمای اتاق
room_temperature['cold'] = fuzz.trapmf(room_temperature.universe, [0, 0, 15, 20])
room_temperature['comfortable'] = fuzz.trimf(room_temperature.universe, [18, 22, 26])
room_temperature['hot'] = fuzz.trapmf(room_temperature.universe, [24, 30, 40, 40])

# تعریف توابع عضویت برای سرعت فن
fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [30, 50, 70])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [50, 100, 100])

# تعریف توابع عضویت برای حالت سیستم
mode['cooling'] = fuzz.trimf(mode.universe, [0, 0, 1])
mode['heating'] = fuzz.trimf(mode.universe, [1, 1, 2])
mode['fan_only'] = fuzz.trimf(mode.universe, [2, 2, 2])

# تعریف قوانین فازی
rule1 = ctrl.Rule(room_temperature['cold'], (fan_speed['low'], mode['heating']))
rule2 = ctrl.Rule(room_temperature['comfortable'], (fan_speed['low'], mode['fan_only']))
rule3 = ctrl.Rule(room_temperature['hot'], (fan_speed['high'], mode['cooling']))

# سیستم کنترل فازی
temperature_control = ctrl.ControlSystem([rule1, rule2, rule3])
temp_simulation = ctrl.ControlSystemSimulation(temperature_control)

def forward_chaining(temp):
    """
    Forward chaining to determine system actions based on room temperature.
    """
    temp_simulation.input['room_temperature'] = temp
    temp_simulation.compute()
    fan = temp_simulation.output['fan_speed']
    system_mode = temp_simulation.output['mode']
    return fan, system_mode

def backward_chaining(target_mode, temp_range):
    """
    Backward chaining to find temperature ranges that trigger a target mode.
    """
    results = []
    for temp in temp_range:
        temp_simulation.input['room_temperature'] = temp
        temp_simulation.compute()
        if round(temp_simulation.output['mode']) == target_mode:
            results.append(temp)
    return results

# اجرای سیستم
if __name__ == "__main__":
    print("Forward Chaining Example:")
    temp = float(input("Enter current room temperature (°C): "))
    fan_speed, mode = forward_chaining(temp)
    mode_str = {0: "Cooling", 1: "Heating", 2: "Fan Only"}
    print(f"Fan Speed: {fan_speed:.2f}%")
    print(f"System Mode: {mode_str[round(mode)]}")

    print("\nBackward Chaining Example:")
    target_mode = int(input("Enter target mode (0: Cooling, 1: Heating, 2: Fan Only): "))
    temp_range = np.arange(0, 41, 1)
    valid_temps = backward_chaining(target_mode, temp_range)
    print(f"Temperatures that trigger mode {mode_str[target_mode]}: {valid_temps}")
