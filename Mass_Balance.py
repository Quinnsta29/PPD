# Description: This script calculates the production rate of ethylamine, water, ammonia and ethanol in the production of ethylamine from ethanol and ammonia.
# Convert production rate to ton/hour
Delfzijl_production_rate = 55000 # ton/year
Delfzijl_production_rate = Delfzijl_production_rate / 365.25 # ton/day
Delfzijl_production_rate = Delfzijl_production_rate / 24 # ton/hour

# incorporate the yield of the reaction
ethylamine_yield = 0.9 # kg/kg
production_rate_ethylamine = Delfzijl_production_rate / ethylamine_yield # ton/hour
production_rate_ethylamine_copy = production_rate_ethylamine
# print(f'{production_rate_ethylamine} ton ethylamine/hour')

# Molecular weights
mw_ethylamine = 45.0837 # g/mol
mw_water = 18.01528 # g/mol
mw_ammonia = 17.0305 # g/mol
mw_ethanol = 46.0684 # g/mol

# Calculate the theoretical production rate in mol/hour
production_rate_ethylamine = production_rate_ethylamine * 1000 # kg/hour
production_rate_ethylamine = production_rate_ethylamine * 1000 # g/hour
production_rate_ethylamine = production_rate_ethylamine / mw_ethylamine # mol/hour

print('Theoretical production rate in mol/hour:')
print(f'{production_rate_ethylamine} mol ethylamine/hour \n')


# C2H5OH + NH3 -> C2H5NH2 + H2O
# 1 mol + 1 mol -> 1 mol + 1 mol
production_rate_water = production_rate_ethylamine * 1 # mol/hour
production_rate_ethanol = production_rate_ethylamine * 1 # mol/hour
production_rate_ammonia = production_rate_ethylamine * 1 # mol/hour

# Calculate the production rate in ton/hour
production_rate_water = production_rate_water * mw_water # g/hour
production_rate_water = production_rate_water / 1000 # kg/hour
production_rate_water = production_rate_water / 1000 # ton/hour
production_rate_ethanol = production_rate_ethanol * mw_ethanol # g/hour
production_rate_ethanol = production_rate_ethanol / 1000 # kg/hour
production_rate_ethanol = production_rate_ethanol / 1000 # ton/hour
production_rate_ammonia = production_rate_ammonia * mw_ammonia # g/hour
production_rate_ammonia = production_rate_ammonia / 1000 # kg/hour
production_rate_ammonia = production_rate_ammonia / 1000 # ton/hour

print('Flow rates in ton/hr')
print(f'{production_rate_ethylamine_copy} ton ethylamine/hour')
print(f'{production_rate_water} ton water/hour')
print(f'{production_rate_ethanol} ton ethanol/hour')
print(f'{production_rate_ammonia} ton ammonia/hour \n')

print('Check the mass balance:')
print("water + ethylamine")
print(production_rate_water + production_rate_ethylamine_copy)
print("ethanol + ammonia")
print(production_rate_ethanol + production_rate_ammonia)