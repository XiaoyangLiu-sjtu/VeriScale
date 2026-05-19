# VeriScale

📝 Official implementation of the paper:

**VeriScale: Adversarial Test-Suite Scaling for Verifiable Code Generation**


## Dataset Downloads
By applying the VeriScale framework to the [Verina](https://github.com/sunblaze-ucb/verina) benchmark (commit hash: `e4f2cf518b4951eb9f66ae3ca0f0be8c4903580d`), we have constructed two augmented datasets by scaling the original test suites. You can find all datasets located under the `dataset/` directory.
- Verina: The original dataset to be scaled.
- VerinaPlus: A comprehensive expansion scaling the original test suites by over 83x.
- VerinaLite: A lightweight variant offering a 14x expansion.


## Project Structure

The repository is organized as follows.

```text
VeriScale/
├── dataset/                          
│   ├── verinaplus/                   # Expanded Verina to construct VerinaPlus
│   └── verinalite/                   # Distilled VerinaPlus to construct VerinaLite
├── src/                              
│   ├── input/                        # Input expansion stage
│   │   ├── step1_llm_generation.py
│   │   ├── step2_type_mutation.py
│   │   └── step3_lean_filters.py
│   └── output/                       # Output expansion stage
│       ├── prompt_config_adversarial.py
│       ├── step1_problem_model.py
│       ├── step2_problem_spec.py
│       ├── step3_problem_adversarial.py
│       ├── step4_accept_output.py
│       └── step5_reject_output.py
├── expand_inputs.py                  # Executes the full input expansion stage
├── expand_outputs.py                 # Executes the full output expansion stage
├── reduce_pairs.py                   # Adversary-killing reduction strategy
├── reduce_unexpected_inputs.py       # Boundary-preserving reduction strategy
├── verinaplus.py                     # Builds VerinaPlus from expanded benchmark artifacts
├── verinalite.py                     # Builds VerinaLite from VerinaPlus
├── utils.py                          # Shared utility functions
├── Verina.lean                       
├── lakefile.lean                     
├── lake-manifest.json                
├── lean-toolchain                    
└── README.md
```


## Quick Start
1. **Install Lean4.** Follow the official [Lean4 installation guide](https://leanprover-community.github.io/get_started.html).
2. **Clone the repository.** Clone this repository and enter the project directory.
3. **Build the project.** Run the following commands to prepare dependencies.
    ```bash
    lake exe cache get
    lake update
    ```
4. **Scale the test suites.** Run the following commands in order to scale the test suites and construct VerinaPlus and VerinaLite.
    ```bash
    python expand_inputs.py
    python expand_outputs.py
    python verinaplus.py
    python verinalite.py
    ```
5. **Evaluation.** Use the official evaluation harness provided by [VERINA](https://github.com/sunblaze-ucb/verina) to evaluate the performance of the model capabilities on the original and augmented datasets. See the Verina repository for the specific evaluation scripts.