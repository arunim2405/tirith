import BaseEvaluator

# Checks if :attr:`value` is less then or equal to :attr:`other`. Automatically casts values to the same type if possible.

# Args:
#     value (mixed): Value to compare.
#     other (mixed): Other value to compare.

# Returns:
#     bool: Whether :attr:`value` is less then equal to :attr:`other`.

# Example:

#     >>> eq(None, None)
#     True
#     >>> eq(None, '')
#     False
#     >>> eq('a', 'a')
#     True
#     >>> eq(1, str(1))
#     False

# .. versionadded:: 1.0.0


class LessThanEqualTo(BaseEvaluator):
    def evaluate(self, evaluator_input, evaluator_data):
        evaluation_result = {"result": False, "message": "LessThanEqualTo evaluator failed"}
        try:
            value1 = evaluator_input
            value2 = evaluator_data
            evaluation_result["result"] = value1 <= value2
            return evaluation_result
        except Exception as e:
            evaluation_result["message"] = str(e)
            return evaluation_result