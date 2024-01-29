import pandas as pd
from graph import Graph

def convert_dtype(val):
    """Attempt to convert the value to an integer or a float, fall back to string if fails."""
    try:
        # First, try converting to float
        float_val = float(val)
        # If the float value is equivalent to an integer, return as int
        if float_val.is_integer():
            return int(float_val)
        else:
            return float_val
    except ValueError:
        # If conversion to float fails, return as string
        return val

def execute_test(stimuli_file, actuation_file):
    df = pd.read_csv(stimuli_file)
    calc = Graph()  # Create an instance
    results = []

    for _, row in df.iterrows():
        func_name = row['B']
        # Convert parameters dynamically and store in a list
        params = [convert_dtype(param) for param in row[df.columns[4:]].dropna().tolist()]

        if hasattr(calc, func_name):
            func = getattr(calc, func_name)
            try:
                result = func(*params)
            except Exception as e:
                result = str(e)
        else:
            result = "Function not found"

        results.append(result)

    # Insert results into column 'A'
    df['A'] = results
    # Save the DataFrame to a CSV, excluding the unnamed index
    df.to_csv(actuation_file, index=False)

# Example usage
execute_test('stimuli.csv', 'actuation.csv')
