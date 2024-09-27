
# Installation

1. Copy `.env.example` to `.env` and add your OpenAI API key.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

# Run the Project

- To upload training data: 

   ```bash
   python3 upload_file.py
   ```

- To start fine-tuning:

   ```bash
   python3 fine-tune.py
   ```

- To get training evaluation data:

   ```bash
   python3 get_evaluation.py
   ```

- To check or test:

   ```bash
   python3 check.py
   ```
