# Text to Math Problem Solving Using Gemma 2 📈

This project leverages **Gemma 2** from Groq and LangChain tools to create an intelligent chatbot capable of solving mathematical problems, providing logical reasoning, and fetching relevant information from Wikipedia. The application is built using **Streamlit** for a seamless user interface.

## Features

- **Mathematical Problem Solving**: Solve complex math problems using Gemma 2's advanced capabilities.
- **Logical Reasoning**: Provide detailed, point-wise explanations for problem-solving.
- **Wikipedia Integration**: Fetch information from Wikipedia to complement reasoning and calculations.
- **Interactive Chat Interface**: Engage with a chatbot that maintains conversational context using Streamlit's session state.
- **Real-Time Output**: View detailed reasoning and step-by-step problem-solving.

## Tools and Technologies

- **LangChain**:
  - Wikipedia API Wrapper
  - Tool Initialization
  - LLMMathChain
  - PromptTemplate
- **Gemma 2 (Groq)**: A powerful language model used for problem-solving.
- **Streamlit**: Provides an interactive and user-friendly web interface.
- **Session State**: Retains conversation history for seamless interactions.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/alihassanml/llm-math-problem-solving.git
   ```
2. Navigate to the project directory:
   ```bash
   cd llm-math-problem-solving
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   streamlit run app.py
   ```
2. Open your browser to the URL displayed in the terminal.
3. Enter a math question or logical query in the text area and get detailed responses.

## Example

### Input:
```
What is the sum of 15 and 25?
```

### Output:
```
Answer:
- Step 1: Identify the numbers to add (15 and 25).
- Step 2: Perform the addition: 15 + 25 = 40.
- Final Answer: 40.
```

## Project Structure

- `app.py`: Main application file containing the Streamlit code.
- `README.md`: Documentation for the repository.
- `requirements.txt`: Python dependencies.

## Contributing

Contributions are welcome! Feel free to fork this repository, make changes, and create a pull request.

## License

This project is licensed under the MIT License.

## Contact

- **Author**: Ali Hassan  
- **GitHub**: [Ali Hassan](https://github.com/alihassanml)  
- **Location**: Lahore, Pakistan  

Explore the app, solve math problems, and enhance logical reasoning! 🚀
