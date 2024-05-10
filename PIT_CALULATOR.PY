class tax_calculate:
    def __init__(self):
            pass
    # fuction to calculate income tax based on income slabs
    def calculation_income_tax(self,income):
        if income <= 300000:
            return 0
        elif 300001 <=income <= 400000:
            return (income * .1)
        elif 400001 <= income <= 650000:
            return (income * .15)
        elif 650001 <= income <= 1000000:
         return (income * .2)
        elif 1000001 <= income <= 1500000:
            return (income * .25)
        else: income <= 1500001 
        return (income * .30)

class PIT_calculator(tax_calculate):
    # constructor to initialize to employee details
    def __init__(self,name,organisation_name, income,regular,organisation_type,married_status,is_children, children):
        self.name = name
        self.organisation_name = organisation_name
        self.income = income
        self.regular = regular
        self.organisation_type = organisation_type
        self.married_status = married_status
        self.is_children = is_children
        self.children = children
        
    def calculate_deduction(self):
         # annual amount of NU 2400 of GIS contribution shall be deductible.
        # 5% of  PF contribution shall be deductible
        deduction =  0
       # checking the employee type and organisation type for PF and GIS deduction
        if self.regular:
            if self.organisation_type == 'govt':
                deduction +=self.income* 0.05
                deduction += 2400
            if self.organisation_type == 'private':
                deduction += self.income* .05
            elif self.organisation_type == 'corporate':
                deduction += self.income* .05
        elif not self.regular:
            if self.organisation_type == 'private':
                deduction += self.income* .05
            elif self.organisation_type == 'corporate':
                deduction += self.income* .05
        else:
            print('No deduction for PF and GIS')
        # children education allowance deduction 
        education_allowance = 0
        if  self.children and isinstance(self.children,int) and self.children > 0:
            education_allowance +=self.children * 350000
        else:print('no deduction for children education allowance')
        deduction += education_allowance
    
        return deduction
    
    def calculate_tax(self):
        #function to calculate final tax payable 
        deduction = self.calculate_deduction()
        taxable_income = self.income - deduction #self.calculate_deduction()
        tax = self.calculation_income_tax(taxable_income)
        if tax >= 1000000:
            tax += tax * 0.1  # Surcharge of 10% for income more than 1000000
        return tax
def main():
    # Get user input
    name = input('enter your name:')
    organisation_name = input ('Enter your organisation name:')
    income = int(input("Enter employee monthly income: ")) * 12 # convert annual income
    regular = input("Is employee a regular employee? (y/n): ").lower() == 'y'
    organization_type = input("Enter organization type (govt/private/corporate): ").lower()
    married_status = input('Is employee married? (yes/no): ').lower() == 'yes'        
    is_children = input ('Is children going to school? (y/n):').lower == 'y'
    children = int(input("Enter number of children: "))

    # Create an Employee object
    employee = PIT_calculator(name, organisation_name,income, regular, organization_type, married_status,is_children, children)

    # Calculate and display tax payable
    tax_payable = employee.calculate_tax()
    
    print(f"Tax payable for employee {name} working under {organisation_name} is Nu. {tax_payable}")

main()#call the main function to run the program