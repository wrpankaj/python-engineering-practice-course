class EfficiencyCalculator:
    def general_efficiency(self, output, input_):
        if input_ == 0:
            return None
        return (output / input_) * 100

    def mechanical_efficiency(self, output_power, input_power):
        return self.general_efficiency(output_power, input_power)

    def boiler_efficiency(self, heat_output, heat_input):
        return self.general_efficiency(heat_output, heat_input)

    def pump_efficiency(self, rho, g, Q, H, input_power):
        hydraulic_power = rho * g * Q * H
        return self.general_efficiency(hydraulic_power, input_power)


calc = EfficiencyCalculator()

print("Mechanical Efficiency =", calc.mechanical_efficiency(750, 1000), "%")
print("Boiler Efficiency =", calc.boiler_efficiency(9000, 12000), "%")
print("Pump Efficiency =", calc.pump_efficiency(1000, 9.81, 0.02, 20, 5000), "%")
