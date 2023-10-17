import pandas as pd

# Load your CSV dataset into a Pandas DataFrame
df = pd.read_csv('missing_migrants.csv')

cod_mapping = {
    "Accidental death": "Accidental death",
    "Drowning": "Drowning",
    "Drowning,Harsh environmental conditions / lack of adequate shelter, food, water": "Drowning",
    "Drowning,Mixed or unknown": "Drowning",
    "Drowning,Sickness / lack of access to adequate healthcare": "Drowning",
    "Drowning,Vehicle accident / death linked to hazardous transport": "Drowning",
    "Drowning,Violence": "Drowning",
    "Harsh environmental conditions / lack of adequate shelter, food, water,Sickness / lack of access to adequate healthcare": "Harsh environmental conditions",
    "Harsh environmental conditions / lack of adequate shelter, food, water,Mixed or unknown": "Harsh environmental conditions",
    "Harsh environmental conditions / lack of adequate shelter, food, water": "Harsh environmental conditions",
    "Mixed or unknown": "Mixed or unknown",
    "Mixed or unknown,Vehicle accident / death linked to hazardous transport,Violence": "Mixed or unknown",
    "Sickness / lack of access to adequate healthcare": "Sickness",
    "Vehicle accident / death linked to hazardous transport": "Vehicle accident / Hazardous transport",
    "Violence": "Violence"
}


df['grouped_cod'] = df['Cause of Death'].map(cod_mapping)

df.to_csv('grouped_cod_missing_migrants.csv', index=False)
