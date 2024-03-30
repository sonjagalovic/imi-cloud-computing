cwlVersion: v1.2
class: CommandLineTool
baseCommand: ["python", "/app/preprocessing.py"]

hints:
  DockerRequirement:
    dockerPull: sonjagalovic/racunarstvo-u-oblaku:assignment3

inputs:
  dataset_file:
    type: File
    inputBinding:
      position: 1

outputs:
  cleaned_dataset:
    type: stdout
stdout: cleaned_dataset.csv