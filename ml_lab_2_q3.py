a = int(input("Enter the number of categorical variables: "))
categorical_variables = []
for i in range(a):
    var = input(f"Enter the {i+1}th categorical variable: ")
    categorical_variables.append(var)

def numeric_variable_mapping(categories):
    numeric_mapping = {}
    for i, category in enumerate(categories):
        numeric_mapping[category] = i
    return numeric_mapping

numeric_mapping = numeric_variable_mapping(categorical_variables)
print("Categorical variable => Numeric variable:")
for category, numeric_value in numeric_mapping.items():
    print(f"{category} => {numeric_value}")

#numericresult=numericvariable(a,catogiracalvariables)
#print(catogiracalvariables[i],"=>",numericvariable[i])
