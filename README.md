# TextSummarizer
Step 1: Project Structure Generator

1- clone the repository using:
    git clone

2- on vs-code create and activate a new environment using:
    conda create -p nenv python=3.14 -y
    conda activate nenv/

3- Create requirements.txt  including libraries and packegaes needed for project, and install it using:
    pip install -r requirements.txt

4- Create template.py as a project structure generator and run it using:
    python template.py

5- Create .gitignore file manually including:
    nenv/
    artifacts/

6- Tracking:
    git add .
    git commit -m "Project Structure"
    git push origin main
    git status

Step 2: Implementing logging ....> src/textSummerizer/logging/__init__.py

Step 3: Implementing utility functions ....> src/textSummerizer/utils/common.py

Step 4: TextSummerizer using Huggingface
### Workflows
1. config.yaml
2. params.yaml
3. Config entity
4. Configuration manager
5. Update components--> Data Ingestion, Data Transformation, Model Trainer
6. Create pipeline --> Training pipeline, Prediction pipeline
7. Front end 



