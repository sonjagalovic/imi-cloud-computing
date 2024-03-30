cwlVersion: v1.2
class: CommandLineTool
baseCommand: ["python", "/app/training.py"]

hints:
  DockerRequirement:
    dockerPull: sonjagalovic/racunarstvo-u-oblaku:assignment3
inputs:
  cleaned_dataset:
    type: File
    inputBinding:
      position: 1
  target_column:
    type: string
    inputBinding:
      position: 2
  training_percentage:
    type: float
    inputBinding:
      position: 3

outputs:
  performance_metrics:
    type: stdout
stdout: performance_metrics.txt