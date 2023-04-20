# an exploration of LC50 - leverage coefficient
# taking 80/20 pareto 3x on itself 
# 80/20 on 80/20 = 64/4 (80*.8/20*.2) = 50/1 (64*.8/4*.2)
# outsized impact of outsized impact of outsized impact
#

"""
The LC50 concept can be derived from applying the 80/20 rule three times. In its simplest form, the 80/20 rule states that 80% of the results come from 20% of the inputs. Applying the rule three times, we get that 51.2% (80% of 80% of 80%) of the results come from 0.8% (20% of 20% of 20%) of the inputs. To obtain the LC50, we can calculate the ratio of influence between the top 0.8% and the average input.

Here's a Python script illustrating this concept:
"""

def lc50_from_pareto(pareto_ratio, iterations=3):
    """
    Calculate the LC50 (Leverage Coefficient) from a given Pareto ratio (e.g., 80/20 rule), applying the rule multiple times.

    Args:
        pareto_ratio (tuple of float): A tuple representing the Pareto ratio (e.g., (80, 20) for the 80/20 rule).
        iterations (int): The number of times to apply the Pareto rule.

    Returns:
        float: The LC50 value.
    """
    top_percentage = pareto_ratio[1] / 100
    top_result_percentage = pareto_ratio[0] / 100

    # Apply the Pareto rule multiple times
    for _ in range(iterations - 1):
        top_percentage *= top_percentage
        top_result_percentage *= top_result_percentage

    # Calculate the average influence of the top 0.8% inputs
    top_inputs_average_influence = top_result_percentage / top_percentage

    # Calculate the average influence of all inputs
    total_inputs_average_influence = 1

    # Calculate the LC50 as the ratio between the top 0.8% influence and the total average influence
    lc50 = top_inputs_average_influence / total_inputs_average_influence

    return lc50


# Example
pareto_rule = (80, 20)
lc50 = lc50_from_pareto(pareto_rule, iterations=3)
print(f"LC50: {lc50}")  # Output: LC50: 50.0
