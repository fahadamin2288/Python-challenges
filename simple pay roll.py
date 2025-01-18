from abc import ABC, abstractmethod
from typing import List


class Employee(ABC):
    def __init__(self, name: str, employee_id: int):
        self.name = name
        self.employee_id = employee_id
        self.salary = 0.0

    @abstractmethod
    def calculate_salary(self) -> float:
        pass


class HourlyEmployee(Employee):
    def __init__(self, name: str, employee_id: int, hours_worked: float, hourly_rate: float):
        super().__init__(name, employee_id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self) -> float:
        self.salary = self.hours_worked * self.hourly_rate
        return f"For Hourly Employee:\n        {self.name} total salary is {self.salary}"


class SalariedEmployee(Employee):
    def __init__(self, name: str, employee_id: int, fixed_salary: float):
        super().__init__(name, employee_id)
        self.fixed_salary = fixed_salary

    def calculate_salary(self) -> float:
        self.salary = self.fixed_salary
        return f"For Salaried Employee:\n        {self.name} total salary is {self.salary}"


class PayrollSystem:
    @staticmethod
    def calculate_payroll(employees: List[Employee]) -> float:
        for employee in employees:
            x = employee.calculate_salary()
            print(x)


hour_emp = HourlyEmployee("Fahad", 6350, 8, 250)
salar_emp = SalariedEmployee("Zain", 1710, 50000)

total_payroll = PayrollSystem.calculate_payroll([hour_emp, salar_emp])
