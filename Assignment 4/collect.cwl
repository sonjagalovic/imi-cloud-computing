cwlVersion: v1.2
class: CommandLineTool
baseCommand: ["python", "/app/collect.py"]

hints:
  DockerRequirement:
    dockerPull: sonjagalovic/racunarstvo-u-oblaku:assignment4

inputs:
  metrics:
    type: string[]
    inputBinding:
      position: 1

outputs:
  output_final:
    type: stdout
stdout: rezultati.txt