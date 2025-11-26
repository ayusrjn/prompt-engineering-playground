import yaml

class PromptLibrary:
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            self.raw_prompts = yaml.safe_load(f)
            
    def get_prompt(self, prompt_name, **kwargs):
        """Fetches a template by name and fills it instantly."""
        if prompt_name not in self.raw_prompts:
            raise KeyError(f"Prompt '{prompt_name}' not found in library.")
        
        template = self.raw_prompts[prompt_name]
        
        return templaye.format(**kwargs)
    
    
library = PromptLibrary("prompts.yaml")
final_prompt = library.get_prompt('guardrail_check', input_text="I hate you")
print(final_prompt)