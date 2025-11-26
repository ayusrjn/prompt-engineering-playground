import string

class PromptTemplate:
    def __init__(self, template_str: str):
        self.template_str = template_str
        # Extract variable names automatically to validate inputs later
        self.input_variables = self._extract_variables()

    def _extract_variables(self):
        """Parses the string to find all {variable_names}."""
        formatter = string.Formatter()
        return [
            fname for _, fname, _, _ in formatter.parse(self.template_str) 
            if fname is not None
        ]

    def render(self, **kwargs) -> str:
        """Injects data into the template."""
        # 1. Validation: Check if the user forgot any variables
        missing_vars = [var for var in self.input_variables if var not in kwargs]
        if missing_vars:
            raise ValueError(f"Missing required variables: {missing_vars}")

        # 2. Render: Return the formatted string
        return self.template_str.format(**kwargs)


if __name__ == "__main__":
    # Define a ReAct style template
    react_raw = """
    Question: {user_question}
    Thought: {thought_process}
    Action: {tool_name}
    """
    
    # Initialize the engine
    prompt = PromptTemplate(react_raw)
    
    # Render it
    final_output = prompt.render(
        user_question="What is 2+2?",
        thought_process="I need to use a calculator.",
        tool_name="Calculator"
    )
    
    print(final_output)