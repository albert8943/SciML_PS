# Scientific Machine Learning for Power Systems: Dynamic Modeling, Stability Assessment, and Parameter Estimation

## Course development and research report

**Prepared for:** Dr. Albert Poulose  
**Research cutoff:** 8 October 2026  
**Version:** 1.1 — expanded online-resource guide  
**Updated:** 8 October 2026 — prioritized resources, module mapping, and additional reference links  
**Format:** Graduate course with reproducible computational laboratories

> **Recommended identity:** An engineering course that teaches students to use scientific machine learning to predict power-system dynamics, assess stability, and infer physical parameters. Power-system questions organize the course; mathematical and machine-learning methods support those questions.



## Contents

1. [Executive recommendation](#1-executive-recommendation)
2. [Research scope and evidence](#2-research-scope-and-evidence)
3. [Course identity and learning outcomes](#3-course-identity-and-learning-outcomes)
4. [Conceptual and mathematical framework](#4-conceptual-and-mathematical-framework)
5. [Detailed 16-week syllabus](#5-detailed-16-week-syllabus)
6. [Laboratory and benchmark design](#6-laboratory-and-benchmark-design)
7. [Assessment and capstone projects](#7-assessment-and-capstone-projects)
8. [Textbooks and reference books](#8-textbooks-and-reference-books)
9. [Essential SciML papers](#9-essential-sciml-papers)
10. [Power-system application papers](#10-power-system-application-papers)
11. [Existing courses and online materials](#11-existing-courses-and-online-materials)
12. [Videos and suggested viewing sequence](#12-videos-and-suggested-viewing-sequence)
13. [Reuse and adaptation plan](#13-reuse-and-adaptation-plan)
14. [Software and reproducibility](#14-software-and-reproducibility)
15. [Scientific validation requirements](#15-scientific-validation-requirements)
16. [Instructor preparation and development roadmap](#16-instructor-preparation-and-development-roadmap)
17. [Advanced extensions and maintenance](#17-advanced-extensions-and-maintenance)
18. [Reference directory](#18-reference-directory)



## 1. Executive recommendation

Develop one coherent course around three application categories:


| Category                                                     | Engineering question                                                             | Main outputs                                                                                   |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **SciML for dynamic modeling and simulation**                | How will the system evolve under specified inputs, parameters, and disturbances? | State trajectories, learned vector fields, hybrid dynamic models, parameterized response maps  |
| **SciML for stability assessment**                           | Will the system remain stable, and how close is it to a stability boundary?      | Stable/unstable decisions, critical clearing time (CCT), empirical stability boundaries        |
| **SciML for parameter estimation and system identification** | Which parameters and dynamic relationships explain the measurements?             | Inertia/damping estimates, controller parameters, learned missing terms, uncertainty estimates |


The first offering should have a strong synchronous-machine core, one multimachine extension, and one reduced-order converter case study. Use an SMIB system repeatedly so students can see how the same equations lead to different learning problems. The capstone can move to a larger system after the method has been validated on the smaller one.

**Recommended delivery:** 16 weeks; 32 lecture hours and 16 guided laboratory hours, with approximately 3–5 hours of independent work each week. Credit allocation should follow the host institution's rules.

**Recommended development strategy:** Build five reliable assignments before expanding the number of methods. Use PyTorch as the common teaching framework, a transparent numerical SMIB implementation for early labs, and a pinned power-system simulator for network experiments.

**Recommended reading architecture:** two primary references, selected supporting book sections, approximately 10 required paper excerpts, and optional specialist readings. The larger bibliography in this report is an instructor resource, not a requirement that every student read every source.

The closest materials found are complementary rather than identical to this proposed course: SciML courses provide computational methods; NPTEL courses provide power-system foundations; power-system research papers supply application case studies. This search did not establish that no equivalent course exists anywhere. It did identify a useful opportunity for a unified, reproducible teaching sequence around the three categories above. [C1–C12; P1–P7]

## 2. Research scope and evidence

This report combines the course decisions confirmed in the conversation with targeted web research. Searches covered official university course pages, author repositories, publisher pages, arXiv records, IEEE education resources, NPTEL, and official software documentation.

Priority was given to sources with identifiable authors/institutions, direct learning materials, a useful match to the syllabus, and sufficiently clear access conditions. References are linked to their original sources wherever possible.

**Evidence labels used in this report:**

- **Checked:** the relevant source page or repository was retrieved, and the stated feature appeared there.
- **Indexed/partial:** an official source was found through search, but direct retrieval was incomplete or some linked material was not inspected.
- **Preprint:** the linked record is a manuscript, and peer-reviewed publication is not assumed.
- **Proposed:** a curriculum, laboratory, assessment, or development recommendation created for this course.

Course links were researched as of the cutoff date. A publicly accessible page is not proof that all recordings play, every notebook runs, enrollment is currently open, or redistribution is permitted. No external notebook was executed during this research. This is a curriculum-development review, not a systematic literature review or a replication study. Some paper recommendations are based on abstracts, bibliographic records, and associated code descriptions rather than a complete technical audit.

A useful version-control finding: arXiv:2602.09667 has a revised title in its April 2026 version, different from its initial search-index title. The directory below uses the title on the retrieved current record. [P7]

## 3. Course identity and learning outcomes



### 3.1 Course description

This course develops scientific machine-learning methods for power-system dynamic modeling, stability assessment, and parameter estimation. Students combine differential-algebraic models, measurements, numerical simulation, automatic differentiation, and machine learning to construct and evaluate predictive and inverse models. Applications include rotor-angle trajectories, inertia and damping identification, critical clearing time, multimachine dynamics, and a selected converter-control example. The course emphasizes conventional baselines, physical consistency, identifiability, reproducibility, and the limits of extrapolation.

### 3.2 Audience and prerequisites

The intended audience is master's students, doctoral students, and researchers in electrical engineering. Students should understand per-unit quantities, power flow, basic synchronous-machine dynamics, ODEs, linear algebra, elementary probability, and Python programming.

Offer a preparatory package with four notebooks: Python/NumPy, numerical integration, neural-network regression, and gradient-based optimization. Include a diagnostic exercise requiring students to simulate a damped oscillator and fit a simple regression model. Students needing substantial introductory programming should complete a bridge course first.

### 3.3 Measurable outcomes

By the end, students should be able to:

1. Formulate forward, inverse, and stability-assessment problems from a specified power-system model.
2. Construct reproducible numerical reference trajectories with explicit event handling.
3. Implement and explain a supervised surrogate, a PINN, and a solver-based learned dynamic model.
4. Implement a basic operator-learning example and explain the input family over which it generalizes.
5. Evaluate the identifiability of selected parameters from specified measurement channels.
6. Distinguish trajectory accuracy, physical residuals, stability decisions, and boundary accuracy.
7. Compare methods using fair data, computational budgets, and engineering metrics.
8. Report uncertainty, failure conditions, and reproducibility information.



### 3.4 Boundaries of the first offering

Transient rotor-angle stability receives the deepest treatment. Frequency response supports inverse estimation. Converter synchronization is an extension. Small-signal stability supplies a useful local check and elective project direction. Comprehensive voltage stability, protection coordination, optimal power flow, electricity markets, load forecasting, and reinforcement-learning control are outside the core.

Use the IEEE stability classification reference to situate the selected topics in the broader field. A course centered on transient rotor-angle assessment should not imply coverage of every stability phenomenon. [P0]

## 4. Conceptual and mathematical framework



### 4.1 Shared system representation

Use a mode-dependent differential-algebraic model:

$$
\dot{x}=f_q(x,z,u;\theta),\qquad 0=g_q(x,z,u;\theta),
$$

$$
y_k=h(x(t_k),z(t_k);\theta)+\varepsilon_k.
$$

Here, $x$ contains dynamic states, $z$ algebraic variables, $u$ inputs, $\theta$ physical parameters, and $q$ the operating mode or network configuration. Fault inception, clearing, switching, and controller limits can change the governing equations. Measurements are produced by an explicit observation model.

Under an idealized switching model, many dynamic states remain continuous while algebraic variables can change immediately. Students must derive continuity or reset conditions from their chosen model. They should not force every output to be smooth across a fault event.

For an introductory SMIB implementation, one consistent convention is:

$$
\dot{\delta}=\omega_b\Delta\omega,\qquad
2H\dot{\Delta\omega}=P_m-P_{e,q}(\delta)-D\Delta\omega,
$$

where $\Delta\omega$ is per-unit speed deviation, $\omega_b$ is base electrical angular frequency, powers are on a specified common base, and $D$ is consistent with this convention. Explain how equations change when speed is expressed in rad/s. Never compare reported $D$, $M$, or $H$ values across papers without checking their definitions.

### 4.2 Three tasks, distinct objectives


| Task                 | Given                                                | Learn or infer                          | Main evaluation                                                                |
| -------------------- | ---------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------ |
| Forward dynamics     | Model family, initial state, inputs, parameters      | Trajectories or dynamic response model  | State errors, phase error, rollout behavior                                    |
| Stability assessment | Operating point, contingency, clearing configuration | Decision or boundary-related quantity   | False-safe rate, CCT error, robustness near boundary                           |
| Inverse estimation   | Measurements and modeling assumptions                | Parameters, states, or missing dynamics | Parameter recovery, uncertainty, identifiability, independent-event prediction |




### 4.3 Method selection


| Method                            | Appropriate teaching role                               | Limitation to investigate                               |
| --------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| Conventional numerical simulation | Reference and operational baseline                      | Cost across many scenarios; model uncertainty           |
| Supervised neural surrogate       | Essential baseline                                      | Data requirements and extrapolation                     |
| PINN                              | Integrating trajectory data and equation residuals      | Optimization difficulty; residual versus solution error |
| Differentiable physical simulator | Parameter fitting and sensitivity analysis              | Solver differentiation and event handling               |
| Neural ODE                        | Learning the vector field                               | Long-rollout error and structural ambiguity             |
| Hybrid/UDE model                  | Known physics plus unknown contributions                | Learned correction can absorb parameter/model errors    |
| DeepONet                          | Learning a response map across an input-function family | Input representation and distribution shift             |
| Graph model                       | Advanced study of network structure                     | New topologies require explicit evidence                |
| Bayesian or ensemble approach     | Quantifying uncertainty                                 | Calibration and distribution-shift limitations          |


These are teaching recommendations, not a universal ranking. Differentiable programming is the broader computational framework enabling several methods; it is not inherently a competing neural architecture. Teach the distinctions using [R1–R12] and power-system comparisons [P1–P7].

## 5. Detailed 16-week syllabus

The three categories organize the course conceptually. The calendar interleaves them where necessary: inverse estimation follows the first PINN lab because students can reuse the same model and residuals.


| Week | Category             | Lecture focus                                                                                             | Practical output                                | Reading anchors  |
| ---- | -------------------- | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | ---------------- |
| 1    | Shared foundation    | Course tasks; SciML taxonomy; physical models and measurements; stability taxonomy                        | Problem specification and diagnostic notebook   | B1, R1, P0       |
| 2    | Shared foundation    | Swing equations; model hierarchy; ODE/DAE distinction; initialization; prefault/fault-on/postfault stages | Numerical SMIB reference with event log         | B1, B2, C8       |
| 3    | Dynamic modeling     | Dataset design; scenario sampling; normalization; data splitting; supervised baselines                    | Held-out trajectory experiment                  | B3, B4           |
| 4    | Shared foundation    | Automatic differentiation; sensitivities; differentiable integration; finite-difference checks            | Verified parameter gradients on smooth segments | R2, C2, C3       |
| 5    | Dynamic modeling     | PINN residuals; initial conditions; data loss; units; parameterized inputs                                | Forward SMIB PINN                               | R3, P1           |
| 6    | Dynamic modeling     | Scaling; training imbalance; collocation; time windows; event interfaces; ablations                       | Failure diagnosis and improved training         | R4, R5           |
| 7    | Parameter estimation | Joint state/parameter fitting; observation models; excitation; identifiability; noise                     | Inertia/damping estimation versus least squares | B6, P2           |
| 8    | Dynamic modeling     | Neural ODEs; hybrid physics/ML; missing terms; solver-based training                                      | Learned or hybrid vector-field model            | R6, R7, P7       |
| 9    | Dynamic modeling     | Multimachine coupling; algebraic constraints; reference coordinates; network generalization               | Small-network model and residual audit          | B2, P3           |
| 10   | Dynamic modeling     | DeepONet; parameter maps versus operators; physics-informed operator learning                             | Response family across unseen inputs            | R8, R9           |
| 11   | Stability            | Engineering stability labels; CCT reference search; boundary-focused evaluation                           | CCT error and false-safe report                 | B1, P3           |
| 12   | Stability            | Converter synchronization; chosen PLL or GFM reduced-order model; controller limits                       | One converter stability case study              | B7, P4           |
| 13   | Parameter estimation | Filtering versus smoothing; synthetic PMU-like observations; missing data; parameter updating             | Independent-event model validation              | B8, P2, P5       |
| 14   | Integration          | Uncertainty; calibration; out-of-distribution tests; physical consistency; runtime accounting             | Reliability and cost comparison                 | R11, P5          |
| 15   | Advanced seminar     | Choose graph models, structure preservation, or learned models for control; project clinic                | Final ablations and reproducibility check       | R10 or C1/C2     |
| 16   | Integration          | Project presentations and technical defense                                                               | Report, code, data specification, limitations   | Project-specific |




### 5.1 Weeks 1–4: reference models before learning

Students derive the state equations, document measurement channels, and identify the target decision. Show how changing a model convention changes parameter interpretation. Generate fault-stage trajectories with integration restarts at known switching times. Verify results using smaller tolerances or an independent numerical configuration.

The dataset exercise should intentionally demonstrate why random splitting of time samples from the same trajectory produces optimistic results. The corrected split holds out complete operating/disturbance scenarios. Sensitivity work starts on smooth segments, then discusses why derivatives with respect to switching times need additional care.

### 5.2 Weeks 5–10: learn solutions, vector fields, and response families

Begin with a compact PINN students can understand line by line. Record data and residual losses separately. Plot errors around clearing and during later oscillations. Teach hard initial-condition constructions where appropriate, without confusing an initial-condition constraint with a guarantee that the entire learned solution is correct.

In the inverse lab, make both the neural weights and selected physical parameters trainable. Compare this with fitting the same parameters through numerical simulation. Include a weakly excited experiment in which a low measurement error does not imply reliable parameter recovery.

For hybrid modeling, choose a controlled missing term and retain its truth for evaluation. A physically incorrect parameter estimate can be hidden by a flexible correction network; ask students to demonstrate this ambiguity.

Operator learning must define what varies. A fixed-dimensional vector of $H$, $D$, and clearing time is a parameterized surrogate input. To teach function-to-function learning explicitly, vary a forcing or control-input waveform represented at sensors. The practical distinction matters more than the architecture name.

### 5.3 Weeks 11–14: engineering decisions and observations

Use separate stable and unstable test sets close to the reference boundary. A model with low global trajectory error may still misclassify these cases. CCT experiments must specify the fault, clearing action, postfault network, simulation horizon, and stability rule.

For converters, choose one family for implementation. A PLL-based reduced-order model has a directly relevant published case study [P4]. A GFM project is also appropriate, but requires a separately validated model and explicit treatment of any limits or mode switches.

For measurements, begin with synthetic channels derived through $h(\cdot)$. Rotor angle is not a direct generic PMU output. Direct state observations are acceptable for a pedagogical experiment only if labeled as such. A subsequent exercise can use terminal voltage/current, power, or frequency channels with clearly stated observation assumptions.

An offline surrogate plus a dashboard should not be presented as a complete operational digital twin. Teach a limited model-updating workflow with provenance, validation, and a defined update frequency.

## 6. Laboratory and benchmark design



### 6.1 Benchmark progression


| Stage | System                                       | Purpose                                          | Required documentation                                          |
| ----- | -------------------------------------------- | ------------------------------------------------ | --------------------------------------------------------------- |
| A     | SMIB, classical machine                      | Transparent forward/inverse/CCT experiments      | Per-unit base, equations, stage parameters, initial equilibrium |
| B     | WSCC 9-bus with an explicit dynamic data set | Network constraints and coupled-machine behavior | Machine/load models, reference bus, fault and clearing actions  |
| C     | Kundur two-area system                       | Interarea behavior and multimachine reproduction | Exact variant, controls, operating point, disturbances          |
| D     | One reduced-order PLL or GFM system          | Converter synchronization extension              | Reduction assumptions, controller equations, limits             |
| E     | Optional larger network                      | Scaling and generalization                       | Full model provenance and manageable experiment scope           |


Do not make every student implement both B and C. Select one common network benchmark and offer the other for projects. A bus count is not a complete dynamic model. Networks with the same name can use different machine orders, load models, controllers, and event definitions.

### 6.2 Five assessed laboratories

**Lab 1 — Reference simulation and scientific dataset.** Deliver an SMIB simulator, event schedule, dataset manifest, and convergence check. Compare at least two numerical settings. Explain how samples were split by scenario. Retain numerical failures as flagged records rather than silently deleting them.

**Lab 2 — Supervised surrogate versus PINN.** Use matched input/output definitions and a documented training budget. Vary the amount of labeled data. Report trajectory errors, residuals, and error around event interfaces. Include a controlled ablation removing the physics term.

**Lab 3 — Inertia and damping estimation.** Compare inverse PINNs with simulation-based least squares using the same measurements and parameter bounds. Vary noise, observation-window length, and excitation. Plot a two-parameter loss surface or a local sensitivity diagnostic. Test fitted parameters on another disturbance.

**Lab 4 — Generalization of a learned dynamic model.** Choose either hybrid/neural ODE modeling or DeepONet. Define the held-out domain before training. Test longer rollouts or unseen input functions, as appropriate. A simple baseline is mandatory. Students selecting different methods can share findings in a seminar.

**Lab 5 — Stability and CCT.** Create reference labels and CCT brackets, then evaluate a learned approach near the boundary. Report signed and absolute CCT errors, false-safe decisions, and end-to-end costs. Investigate one case in which trajectory and CCT rankings disagree.

### 6.3 Standard experiment record

Each experiment should record a unique scenario ID; model/version; parameter units; operating point; initial state; observation channels; fault type/location; inception/clearing times; postfault topology; solver settings; stability criterion and horizon; dataset split; random seed; model configuration; training budget; software versions; and hardware.

Keep units and physical parameters in metadata rather than relying on notebook comments. Store raw reference outputs separately from normalized training arrays. Save the normalization transform fitted on training data only.

### 6.4 Computational accessibility

Design the default SMIB labs for CPU execution and supply small training datasets. Offer optional GPU runs for larger sweeps. Provide validated checkpoints and precomputed reference trajectories so a student can complete scientific analysis even when training resources are limited. Runtime targets are development goals to measure during piloting, not guarantees made before execution.

## 7. Assessment and capstone projects



### 7.1 Assessment structure


| Component         | Weight | Purpose                                                     |
| ----------------- | ------ | ----------------------------------------------------------- |
| Five laboratories | 40%    | Correct implementation and experimental reasoning           |
| Midterm           | 20%    | Equations, assumptions, identifiability, and interpretation |
| Paper critique    | 10%    | Assess evidence and reproducibility                         |
| Capstone          | 30%    | Integrate engineering questions and SciML methods           |


Capstone rubric: formulation and physical correctness 20%; baseline quality 20%; experiments and validation 25%; interpretation and limitations 15%; reproducibility 10%; communication 10%. A carefully supported negative result can receive full credit.

Project milestones: proposal in week 6, reference baseline in week 9, first results in week 12, ablations in week 15, and final presentation in week 16.

### 7.2 Capstone options


| Project                       | Scientific question                                                                           | Essential baseline                         | Stretch extension                          |
| ----------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------ |
| Boundary-focused TSA          | Does sampling near the boundary improve CCT more efficiently than global trajectory training? | Numerical simulation plus bracketed search | Active acquisition of new simulations      |
| Inertia/damping estimation    | Which channels and excitation levels support reliable recovery?                               | Simulation-based least squares             | Calibrated uncertainty                     |
| Hybrid dynamic model          | Can a missing term be learned without corrupting physical parameter estimates?                | Correct/incorrect physics-only models      | Multiple-event identification              |
| Physics-informed DeepONet     | What input family does the learned response map actually generalize across?                   | Parameterized MLP and numerical solver     | Longer horizon or unseen waveforms         |
| Converter synchronization     | Does a learned reduced model preserve useful stability information?                           | Numerical reduced-order model              | Higher-fidelity validation where available |
| Measurement-informed updating | Does fitting one event improve prediction of another?                                         | Fixed-parameter model                      | Drift detection and selective updates      |


Albert's own trajectory-surrogate/CCT work can provide a motivating instructor case study. Prepare a small, independent teaching implementation and discuss its limitations openly. This report does not re-review the paper or assert additional findings from its full text.

## 8. Textbooks and reference books



### 8.1 Priority bookshelf


| ID  | Reference                                                                                                           | Use in this course                                                  | Access and priority                                            |
| --- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------------------- |
| B1  | Kundur and Malik, **Power System Stability and Control**, 2nd ed.                                                   | Machine models, dynamics, stability fundamentals, reference methods | Publisher/library access; primary engineering reference        |
| B2  | Federico Milano, **Power System Modelling and Scripting** (2010)                                                    | DAE modeling, simulation structure, computational implementation    | Springer/library access; instructor priority                   |
| B3  | Brunton and Kutz, **Data-Driven Science and Engineering**                                                           | Regression, model discovery, dynamics, reduced models               | Book plus public companion resources; primary bridge reference |
| B4  | Christopher Bishop and Hugh Bishop, **Deep Learning: Foundations and Concepts** (2024)                              | Neural networks, optimization, probabilistic foundations            | Official online/book resource; supporting sections             |
| B5  | Thuerey et al., **Physics-based Deep Learning**, online v0.3                                                        | Physical losses, differentiable simulation, practical notebooks     | Public online resource; selected sections                      |
| B6  | Lennart Ljung, **System Identification: Theory for the User**, 2nd ed.                                              | Identification methodology, experiment design, model validation     | Publisher/library access; instructor reference                 |
| B7  | Yazdani and Iravani, **Voltage-Sourced Converters in Power Systems: Modeling, Control, and Applications** (2010)    | Converter modeling and control foundations                          | Wiley/library access; converter extension                      |
| B8  | Särkkä and Svensson, **Bayesian Filtering and Smoothing**, 2nd ed. (2023)                                           | Filtering, smoothing, parameter estimation                          | Author-hosted manuscript and publisher edition; inverse module |
| B9  | Brenan, Campbell, and Petzold, **Numerical Solution of Initial-Value Problems in Differential-Algebraic Equations** | Consistency and DAE numerical foundations                           | SIAM/library access; advanced instructor preparation           |


**Student-facing core:** B1 plus selected B3/B5 sections and assigned papers. B6, B8, and B9 are references for deeper questions; do not require students to buy the complete list.

### 8.2 How to assign book readings

Assign topics rather than unverified chapter numbers: swing equations and transient stability from B1; differential-algebraic formulation and time-domain simulation from B2; regression and data-driven dynamics from B3; gradient computation and training from B4; physical losses and differentiable physics from B5; identifiability and validation from B6; converter frame transformations and controls from B7; nonlinear filtering from B8.

Match chapter numbers to the actual edition used before publishing the student syllabus. Older foundational books remain useful, but supplement converter-era stability terminology and contemporary SciML methods with current papers.

## 9. Essential SciML papers


| ID  | Reference                                                                                                                                                                                                    | Teaching purpose and critical question                                                                                                           |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| R1  | Karniadakis et al., **Physics-informed machine learning**, Nature Reviews Physics (2021)                                                                                                                     | Conceptual overview. Where does physics enter, and what evidence supports the claimed benefit?                                                   |
| R2  | Baydin et al., **Automatic differentiation in machine learning: a survey**                                                                                                                                   | Explain AD versus finite differences and symbolic differentiation. What function is being differentiated?                                        |
| R3  | Raissi, Perdikaris, and Karniadakis, **Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations**, JCP (2019) | Foundational residual formulation. Translate a PDE example into the selected power-system ODE/DAE problem.                                       |
| R4  | Wang et al., **An Expert's Guide to Training Physics-informed Neural Networks** (2023 manuscript)                                                                                                            | Practical training and ablation design. Which improvement helps the chosen problem, and at what cost?                                            |
| R5  | Krishnapriyan et al., **Characterizing possible failure modes in physics-informed neural networks** (2021)                                                                                                   | Failure analysis. Why can a valid equation-based loss still be difficult to optimize?                                                            |
| R6  | Chen et al., **Neural Ordinary Differential Equations** (2018)                                                                                                                                               | Solver-based learned dynamics. How do integration and sensitivity choices affect training?                                                       |
| R7  | Rackauckas et al., **Universal Differential Equations for Scientific Machine Learning** (2020 manuscript; revised 2021)                                                                                      | Hybrid physical/learned models. Which quantities remain physically interpretable?                                                                |
| R8  | Lu et al., **Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators** (2021; linked earlier manuscript has a different title)                                   | Branch/trunk construction. What is the input function and how is it sampled?                                                                     |
| R9  | Wang, Wang, and Perdikaris, **Learning the solution operator of parametric partial differential equations with physics-informed DeepOnets** (2021 manuscript)                                                | Operator learning with residual constraints. What changes when labels are sparse?                                                                |
| R10 | Kovachki et al., **Neural Operator: Learning Maps Between Function Spaces With Applications to PDEs**, JMLR (2023)                                                                                           | Advanced mathematical background. Which assumptions apply to the proposed power-system example?                                                  |
| R11 | Psaros et al., **Uncertainty Quantification in Scientific Machine Learning: Methods, Metrics, and Comparisons** (linked 2022 manuscript)                                                                     | Reliability and calibration. Does a confidence interval have the claimed coverage?                                                               |
| R12 | Kopaničáková and Riccietti, **Introduction to optimization methods for training SciML models** (2026 preprint, v2)                                                                                           | Recent optimization tutorial. Compare first-order and curvature-aware strategies without assuming universal superiority.                         |
| R13 | Brunton, Proctor, and Kutz, **Discovering governing equations from data: Sparse identification of nonlinear dynamical systems** (2016; preprint 2015)                                                        | Optional equation discovery. How do noise, differentiation, and feature-library choices affect recovery?                                         |
| R14 | Li et al., **Fourier Neural Operator for Parametric Partial Differential Equations** (2021; preprint 2020)                                                                                                   | Optional operator architecture. Explain why a spectral spatial model is not automatically the best choice for a small lumped power-system model. |


The required student set can be reduced to R1–R6, R8–R9, and selected excerpts from R11–R12. Use R7 and R10 for project groups going deeper. Paper age is not a quality score; the course should combine enduring ideas with current evaluation practices.

## 10. Power-system application papers



### 10.1 Core application collection


| ID  | Reference and status                                                                                                                                                                                                                                             | Match to the course                                            | Proposed teaching use                                                                     |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| P0  | Hatziargyriou et al., **Definition and Classification of Power System Stability – Revisited & Extended**, IEEE TPWRS (2021)                                                                                                                                      | Stability scope and terminology                                | Assign at the start; distinguish the phenomena actually modeled                           |
| P1  | Misyris, Venzke, and Chatzivasileiadis, **Physics-Informed Neural Networks for Power Systems**, IEEE PES GM (2020); author manuscript 2019                                                                                                                       | Forward states and uncertain parameters                        | Foundational power-system PINN example; associated code available                         |
| P2  | Stiasny, Misyris, and Chatzivasileiadis, **Physics-Informed Neural Networks for Non-linear System Identification for Power System Dynamics**, IEEE PowerTech (2021)                                                                                              | Dynamic state/parameter identification; comparison with UKF    | Critique measurement assumptions and baseline fairness                                    |
| P3  | Stiasny, Misyris, and Chatzivasileiadis, **Transient Stability Analysis with Physics-Informed Neural Networks**, linked manuscript v3 (2023; first posted 2021)                                                                                                  | DAE trajectories and Kundur two-area experiments               | Reproduce a bounded subproblem; distinguish trajectories from direct CCT claims           |
| P4  | Nellikkath et al., **Physics-informed neural networks for phase locked loop transient stability assessment**, EPSR 236, 110790 (2024)                                                                                                                            | Converter PLL trajectories and region-of-attraction assessment | Reduced-order converter case study and recurring prediction                               |
| P5  | Stock et al., **Bayesian Physics-Informed Neural Networks for Robust System Identification of Power Systems**, IEEE PowerTech (2023); manuscript 2022                                                                                                            | SMIB inertia/damping and uncertainty                           | Compare deterministic and probabilistic identification                                    |
| P6  | **Physics-informed machine learning for power system dynamics: A framework incorporating trustworthiness** (2025 publisher record; partially retrieved)                                                                                                          | Reliability-oriented dynamic modeling                          | Supplementary lead for instructor review; not a source for unverified quantitative claims |
| P7  | Kang, Kim, and Yun, **Knowledge Integration in Differentiable Models: A Comparative Study of Data-Driven, Soft-Constrained, and Hard-Constrained Paradigms for Identification and Control of the Single Machine Infinite Bus System**, arXiv:2602.09667v2 (2026) | Direct comparison of modeling approaches on SMIB               | Recent preprint critique; results are specific to its experiments, not universal rankings |
| P8  | **Physics-informed neural networks for power systems: A systematic review** (2026 publisher record; partially retrieved)                                                                                                                                         | Broader power-system literature map                            | Use to discover additional papers, then verify original studies                           |




### 10.2 Reproduction priorities

Start with P1 and P2 for understandable forward/inverse tasks. Use P3 for a multimachine extension and P4 for a converter extension. P5 supports the uncertainty module. P7 is especially relevant for comparing methods but should remain explicitly labeled as a preprint.

Avoid adopting headline speedups or robustness claims as course facts. Recompute accuracy and runtime on the teaching hardware, using the same scenario definition and accounting for training/data generation. Small-system demonstrations motivate methods; they do not establish deployment readiness on a large grid.

### 10.3 Paper critique form

Ask students to report: exact task; governing model; inputs/outputs; available measurements; physical information used; train/test split; comparator; computational budget; uncertainty treatment; reproducibility assets; and one conclusion not justified by the reported evidence. Every review should include a proposed experiment that could falsify the main claim.

## 11. Existing courses and online materials



### 11.1 Source map

The IDs below organize the reference collection; they are not a ranking. Section 11.3 gives the recommended development priorities.


| ID  | Institution/resource                                                                                         | Public material observed                                   | Best use                                                   | Access/reuse qualification                                                                            |
| --- | ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| C1  | **Johns Hopkins: EN.560.652 SciML for Modeling, Optimization, and Control of Dynamical Systems**, Ján Drgoňa | Weekly lecture material and code repository                | Overall differentiable-modeling sequence                   | Checked repository; redistribution license not established in inspected listing                       |
| C2  | **L4DC 2026 SciML tutorial**, Beckers, Nghiem, Drgoňa                                                        | Slides, Colab examples, two YouTube recordings             | Fast instructor orientation; modeling and optional control | Checked organizer page; link to materials, verify permissions before republishing                     |
| C3  | **MIT 18.337J/6.338J SciML**                                                                                 | Notes, homework, lecture links                             | AD, numerical ODEs, stiffness, inverse problems            | Checked; Julia-centered portions require adaptation                                                   |
| C4  | **University of Illinois CS/ME 598 SML, Spring 2026**, Olson and West                                        | Syllabus, notes, demonstrations, assignment topics         | PINN/operator sequence and assignment design               | Checked; a public syllabus is not an open enrollment offer                                            |
| C5  | **ETH Zürich AI in the Sciences and Engineering, HS2026**, with earlier DLSC material                        | Current course page; historical course descriptions/slides | Mathematical SciML depth and operator learning             | Current page checked; historical video access only partially verified                                 |
| C6  | **iAI KAIST Scientific Machine Learning**                                                                    | Editable slides, PDFs, Colab labs, problem sets            | Strongest directly adaptable foundation material found     | Explicit instructor permission to use, modify, distribute on page; some later topics are placeholders |
| C7  | **University of Washington Physics Informed ML Workshop / Brunton–Kutz resources**                           | Workshop program, linked video collection, book resources  | Discovery, reduced models, research seminars               | Checked organizer page; workshop rather than semester course                                          |
| C8  | **IIT Bombay/NPTEL Power System Dynamics and Control**                                                       | Official course page and archived video-course syllabus    | Power-system prerequisites and reference modeling          | Official listing indexed; verify selected lecture availability                                        |
| C9  | **IIT Kharagpur/NPTEL Power System Dynamics, Control and Monitoring**                                        | Official course and syllabus pages                         | Dynamics and monitoring background                         | Indexed/partial; complementary to SciML                                                               |
| C10 | **Oxford Physics Informed Neural Networks, Hilary 2026**                                                     | Official listing describes 16 lectures                     | Mathematical depth for advanced students                   | Indexed/partial; public full recordings not established                                               |
| C11 | **IEEE PES Physics-informed Machine Learning for Power Systems webinar**                                     | Official education listing and slide-resource record       | Domain motivation and broader applications                 | Indexed/partial; login/payment conditions not verified                                                |
| C12 | **Spyros Chatzivasileiadis teaching resources**                                                              | Indexed ML-for-power-systems lecture references            | Domain-specific lecture leads                              | Direct retrieval timed out; do not promise a verified full course                                     |




### 11.2 Recommended adaptation combinations

**Foundations:** C6 provides particularly useful editable starting material; combine with selected C3 explanations and your own power-system derivations. **Dynamic learning:** C1/C2 offer a coherent route through differentiable modeling; translate examples into swing-equation problems. **Operators:** C4 provides a useful teaching sequence, supplemented by R8–R10. **Power systems:** C8/C9 support prerequisites; P1–P5 supply application studies. **Advanced seminars:** C7 and C5 support breadth without enlarging the assessed core.

The new intellectual contribution of the course is the engineering integration: common benchmark definitions; event-aware simulation; measurement assumptions; identifiability; near-boundary errors; and comparisons that use the same physical problem.

### 11.3 Priority online resources: quick-access guide

Use this shortlist when beginning course development. Priorities reflect usefulness for this course, rather than general institutional or research rankings. The proposed adaptations are teaching recommendations, not claims that the original materials already contain these power-system exercises.


| Priority | Resource and direct link                                                                                                                        | Material to use                                                                           | Proposed role in this course                                                                                                                     |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1        | [iAI KAIST — Scientific Machine Learning](https://iailab.kaist.ac.kr/teaching/scientific-machine-learning) [C6]                                 | Editable slides, PDFs, Colab exercises; PINNs, loss weighting, operator learning          | Develop the shared foundations and first PINN lessons; replace generic physical examples with the chosen SMIB model                              |
| 2        | [L4DC 2026 SciML tutorial](https://sciml-l4dc2026.github.io/SciML-L4DC2026/) [C2]                                                               | Recordings, slides, modeling notebooks                                                    | Establish the connection between physics, data, and differentiable modeling; start with Part 1                                                   |
| 3        | [Johns Hopkins SciML course](https://github.com/drgona/SciML-Course) [C1]                                                                       | Weekly lecture material and code                                                          | Structure the progression from PINNs to neural ODEs and constrained models                                                                       |
| 4        | [Physics-Informed Neural Networks for Power Systems](https://github.com/gmisy/Physics-Informed-Neural-Networks-for-Power-Systems) [P1]          | Foundational application code, including parameter-estimation examples                    | Study the forward/inverse formulation and develop a small, maintainable teaching implementation; check the original environment before execution |
| 5        | [Physics-based Deep Learning](https://physicsbaseddeeplearning.org/intro.html) [B5]                                                             | Interactive explanations of physical losses, differentiable physics, and inverse problems | Prepare clear comparisons of ways to incorporate physics; translate selected demonstrations into power-system tasks                              |
| 6        | [MIT Scientific Machine Learning](https://book.sciml.ai/) [C3]                                                                                  | Numerical methods, automatic differentiation, sensitivity and uncertainty material        | Instructor preparation and advanced supporting reading; adapt language/framework where needed                                                    |
| 7        | [Illinois Scientific Machine Learning, Spring 2026](https://github.com/598sml/598sml-s26-syllabus) [C4]                                         | Notes, demonstrations, and assignment topics                                              | Design the DeepONet lesson and optional FNO extension                                                                                            |
| 8        | [Brunton–Kutz companion resources](https://www.databookuw.com/) and [Python notebooks](https://github.com/dynamicslab/databook_python) [B3, S5] | Data-driven modeling examples and companion code                                          | Support system identification, equation discovery, and reduced-order modeling                                                                    |
| 9        | [ANDES documentation](https://docs.andes.app/en/stable/) [S1]                                                                                   | Simulation documentation and tutorials                                                    | Generate numerical reference trajectories and network datasets; freeze a tested version for teaching                                             |


**Recommended starting combination:** KAIST for editable foundations; L4DC/JHU for method explanations; P1 for domain-specific formulation; ANDES for numerical validation. Add MIT, PBDL, and Brunton–Kutz when preparing deeper explanations or project extensions.

The KAIST page's explicit teaching-reuse statement was rechecked for this update. Some later topics still appear as placeholders, so availability should be assessed topic by topic. The Python companion repository was also retrieved; its description identifies the notebooks as companions to the Brunton–Kutz book. No notebook execution was performed for this update.

### 11.4 Power-system-specific tutorial lead: PSCC 2024

The [PSCC 2024 tutorial page](https://www.chatziva.com/pscc2024.html) [C13] is a useful additional domain-specific resource. Its indexed program includes physics-informed neural networks for power-system dynamics and trustworthy AI/ML verification. A related [author-hosted slide PDF](https://www.chatziva.com/PSCC2024Tutorial/3_PSCC2024_Tutorial_Spyros.pdf) was surfaced in the follow-up search.

Use it as supplementary instructor reading for connecting SciML methods with power-system requirements. The tutorial landing page previously timed out, and the slide deck has not been fully reviewed here; complete asset access and redistribution permission remain unverified. Do not describe this as a verified full online course or assume that recordings are available.

### 11.5 Map resources to the three course categories


| Course category                                | Primary resources             | Additional depth | Original teaching output to develop                                                             |
| ---------------------------------------------- | ----------------------------- | ---------------- | ----------------------------------------------------------------------------------------------- |
| Dynamic modeling and simulation                | C1, C2, C6, P1                | B5, C3, C4       | Matched supervised/PINN/neural-ODE experiments on the same dynamic model                        |
| Stability assessment                           | P3, P4, S1; supplementary C13 | B1, P0           | Explicit fault-stage simulations, stable/unstable labels, and near-boundary CCT evaluation      |
| Parameter estimation and system identification | P1, P2, P5, B3/S5             | B6, B8, R11      | Identifiability experiments, conventional estimation baseline, and independent-event validation |


The generic online courses provide method foundations. The power-system papers, numerical benchmarks, and original labs supply the domain-specific stability and estimation content.

## 12. Videos and suggested viewing sequence



### 12.1 Direct or organizer-linked video resources


| Resource                                        | Link                                                                                                   | Status and purpose                                                                                  |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------- |
| L4DC Part 1: introduction and learning to model | [YouTube](https://www.youtube.com/watch?v=fabfvJc5p9M)                                                 | Official repository supplies this link; use for instructor preparation and selected student viewing |
| L4DC Part 2: learning to optimize and control   | [YouTube](https://www.youtube.com/watch?v=MERD-VpN4xw)                                                 | Official repository supplies this link; optional extension                                          |
| UW Physics Informed ML Workshop videos          | [Organizer-linked YouTube collection](https://www.youtube.com/channel/UCAjV5jJzAU8JE4wH7C12s6A/videos) | Research talks; choose specific videos after checking relevance and playback                        |
| Brunton–Kutz companion learning resources       | [Book portal](https://www.databookuw.com/)                                                             | Chapter resources and lecture-video pathways; useful for SINDy and dynamic modeling                 |
| MIT SciML lectures                              | [Lecture index](https://book.sciml.ai/lectures/)                                                       | Follow topic-specific links; especially AD, ODEs, and inverse problems                              |
| NPTEL dynamics course                           | [IIT Bombay course](https://nptel.ac.in/courses/108101004)                                             | Video-course source for prerequisite study                                                          |


Video availability was established through organizer links or course listings, not full playback auditing. Avoid promising subtitles, duration, current certification, or complete unrestricted access without checking the selected resource.

### 12.2 Instructor viewing order

1. Review selected NPTEL dynamics lectures only where a teaching refresh is needed.
2. Watch L4DC Part 1 and map every example to a power-system task.
3. Study MIT AD and differential-equation notes with a small working notebook.
4. Use Brunton–Kutz dynamics/model-discovery material for intuitive explanations.
5. Review operator-learning materials from Illinois and the associated papers.
6. Watch L4DC Part 2 only when preparing an optional control module.

For students, assign one short segment or focused resource per week with a concrete question. Do not prescribe entire video series on top of a full course workload.

## 13. Reuse and adaptation plan



### 13.1 Resource-specific observations


| Source                           | Permission evidence observed                                                                   | Recommended action                                                                                              |
| -------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| iAI KAIST course                 | Page explicitly welcomes instructors to use, modify, and distribute the teaching materials     | Best starting point for editable foundations; retain provenance and check separately credited third-party items |
| NPTEL                            | Current and archived pages show differing Creative Commons notices                             | Check the notice attached to each selected asset; do not assume one license covers all historical materials     |
| JHU, Illinois, L4DC repositories | Public materials observed; a blanket redistribution license was not established in this review | Link and study; obtain/verify terms before copying assets into a public course package                          |
| PBDL and Brunton–Kutz resources  | Public reading/code materials observed                                                         | Check the exact book/code asset terms before adapting or redistributing                                         |
| Journal articles and textbooks   | Access terms depend on publisher/version                                                       | Assign links or library access; create original explanations and figures                                        |
| YouTube recordings               | Official or organizer-linked availability                                                      | Link to recordings; verify permission before downloading, editing, or rehosting                                 |
| ANDES                            | GPL v3 stated in official repository                                                           | Preserve applicable notices and meet license terms for distributed software derivatives                         |
| DeepXDE                          | LGPL-2.1 stated in official repository                                                         | Keep software-license handling separate from teaching-content permissions                                       |


Public availability and attribution alone are not blanket permission to republish. License families differ: check attribution, commercial-use, adaptation, and share-alike requirements for the exact asset. Official Creative Commons guidance is linked as L1. This section is a practical asset-management workflow, not a legal determination for a particular distribution plan.

### 13.2 What to reuse and what to author

Reuse appropriately licensed generic diagrams, introductory AD examples, and basic neural-network exercises. Write original power-system derivations, benchmark specifications, fault-stage illustrations, CCT workflows, measurement models, and assessment questions. Reimplement methods from equations when that improves clarity and maintainability, while citing intellectual sources.

For each adapted asset, record: source URL; authors; exact file; version/commit; license or permission evidence; modifications; attribution text; and whether third-party content is included. Keep this in an attribution register alongside the course repository.

### 13.3 Suggested weekly teaching package

Each week should contain a one-page learning guide; original lecture slides; required reading excerpts; one demonstration notebook; an exercise; expected figures; and a short list of common misconceptions. Add an instructor-only answer key. A reader should be able to distinguish original course material from adapted assets without inspecting commit history.

## 14. Software and reproducibility



### 14.1 Recommended implementation stack


| Layer                             | Proposed choice                | Reason                                                                 |
| --------------------------------- | ------------------------------ | ---------------------------------------------------------------------- |
| Transparent numerical examples    | Python, NumPy, SciPy           | Accessible SMIB equations and reference integrations                   |
| Common ML framework               | PyTorch                        | One consistent learning environment                                    |
| Differentiable ODE extension      | torchdiffeq                    | Companion ecosystem for neural ODEs [S2]                               |
| Network dynamics                  | ANDES, pinned and pilot-tested | Documented power-flow/time-domain/eigenvalue workflow [S1]             |
| Optional PINN/operator toolkit    | DeepXDE                        | Additional examples after students understand the underlying loss [S3] |
| Optional modeling/control toolkit | NeuroMANCER                    | Aligned with C1/C2; unnecessary for every lab [S4]                     |
| Reporting                         | Jupyter, Matplotlib, Markdown  | Executable explanations and reusable reports                           |


Do not require all optional packages in the core environment. Generic ODE tools are not automatically suitable for arbitrary DAEs. For early differentiation exercises use an explicit ODE or a justified reduced model. Network DAE simulation can remain a separate reference/data-generation step. Verify any claimed end-to-end differentiability rather than assuming that an external simulator participates in autodiff.

Official documentation can change its stable version. Pin the tested package versions and the benchmark files for each course release; do not silently switch environments during the semester.

### 14.2 Proposed repository organization


| Directory       | Contents                                             |
| --------------- | ---------------------------------------------------- |
| `syllabus/`     | Course description, calendar, reading list           |
| `lectures/`     | Original slides and attributed adaptations           |
| `notebooks/`    | Numbered demonstrations and exercises                |
| `src/models/`   | SMIB, selected network interface, converter example  |
| `src/training/` | Shared losses, training loops, evaluation            |
| `configs/`      | Model and experiment specifications                  |
| `data/`         | Small redistributable data and manifests             |
| `tests/`        | Physical consistency and numerical regression checks |
| `projects/`     | Project briefs and report template                   |
| `references/`   | Bibliography and attribution register                |


This is a proposed structure, not a repository created by this report. Store substantial datasets through an appropriate research-data release rather than placing every experiment output in Git.

## 15. Scientific validation requirements



### 15.1 Minimum comparison protocol


| Area                 | Required practice                                                                    |
| -------------------- | ------------------------------------------------------------------------------------ |
| Reference simulation | Verify integration settings, event timing, initialization, and algebraic consistency |
| Splits               | Hold out complete trajectories/scenarios; isolate topology tests if claimed          |
| Hyperparameters      | Select using validation data; leave the test set untouched                           |
| Repeated training    | Use multiple seeds when variability affects the conclusion                           |
| Data budget          | Record both labeled trajectories and collocation points                              |
| Physical constraints | Evaluate residuals on points not used during training                                |
| Cost                 | Separate simulation/data generation, training, tuning, inference, and postprocessing |
| Extrapolation        | State whether it concerns time, parameters, inputs, operating points, or topology    |
| Failure reporting    | Include difficult and failed cases with reasons                                      |




### 15.2 Trajectory and stability metrics

Report per-state RMSE/MAE with units or defined normalization; maximum error; phase drift; and horizon-dependent error. An average across differently scaled states can conceal serious errors.

For stability classification, include a confusion matrix and define the false-safe rate explicitly as the fraction of truly unstable cases predicted stable. Accuracy alone can hide an unacceptable imbalance. Test boundary-adjacent scenarios separately from easy cases.

For CCT, report absolute error in milliseconds and signed error:

$$
e_{\mathrm{CCT}}=\widehat{t}_{\mathrm{CCT}}-t_{\mathrm{CCT,ref}}.
$$

A positive error overestimates available clearing time under the defined scenario and criterion. Report the reference bracket width and search tolerance. If a case has no valid bracket, label it rather than inventing a CCT. Simple bisection requires suitable monotonic boundary behavior in the searched interval; complex stability windows require a different search strategy.

Finite-horizon simulation produces an operational label under stated assumptions. It is not a proof of asymptotic stability. A learned classifier or empirical region of attraction likewise requires stronger analysis before being called a certificate.

### 15.3 Inverse-problem checks

Define the observation function, sampling, noise model, unknown inputs, and known parameters. Examine whether several parameter sets produce nearly indistinguishable measurements. Use sensitivity information, profile fits, or controlled parameter sweeps where useful. Constraints such as positive inertia improve plausibility but do not establish identifiability.

When both physical parameters and a neural correction are learned, inspect whether the correction compensates for incorrect parameters. Test predictions on independent events and quantify uncertainty where appropriate. Distinguish aleatoric measurement noise from epistemic/model uncertainty. Ensemble spread alone is not proof of calibrated coverage.

### 15.4 Compute break-even analysis

For a repeated-query application, compare total surrogate cost with conventional simulation over the expected number of queries. A simple estimate is:

$$
N_{\mathrm{break-even}}\approx\frac{C_{\mathrm{data}}+C_{\mathrm{train}}}{C_{\mathrm{reference/query}}-C_{\mathrm{surrogate/query}}},
$$

provided the denominator is positive and costs use comparable hardware and accuracy. Include retraining and validation where they matter. An impressive single-query inference speedup may not justify a model used only a few times.

## 16. Instructor preparation and development roadmap



### 16.1 Eight-stage preparation plan


| Stage | Main work                                             | Reviewable output                             |
| ----- | ----------------------------------------------------- | --------------------------------------------- |
| 1     | Freeze scope, outcomes, conventions, and benchmark    | Course specification and model sheet          |
| 2     | Build numerical SMIB and dataset workflow             | Validated reference notebook                  |
| 3     | Build supervised and PINN baselines                   | Lab 2 with expected plots and failure example |
| 4     | Build inverse estimation and identifiability exercise | Lab 3 and instructor solution                 |
| 5     | Build neural ODE/hybrid and operator demonstrations   | Two small demos; one assessed choice          |
| 6     | Build CCT and network extension                       | Boundary evaluation notebook                  |
| 7     | Add converter, uncertainty, and measurement examples  | Guided specialist notebooks                   |
| 8     | Pilot on clean environments and revise workload       | Versioned release and attribution register    |


These stages can be treated as an initial eight-week development plan if sufficient time is available, but actual duration depends on how much validated teaching code already exists. Do not promise a release date before piloting the central laboratories.

### 16.2 Minimum viable first offering

Finish a complete SMIB forward/inverse/stability sequence first. Then add one network notebook and one converter demonstration. It is better to have six well-tested notebooks with clear baselines than twenty partially working architecture examples.

Suggested first six notebooks: reference dynamics; supervised surrogate; forward PINN; inverse parameter fitting; hybrid/neural ODE; and CCT evaluation. Operator learning can follow once the common data and evaluation interfaces are stable.

### 16.3 Instructor reading sequence

1. B1/B2 and P0: confirm engineering conventions and scope.
2. R1/R3 and P1: build the introductory physics-informed example.
3. R4/R5: prepare a convincing training-failure lesson.
4. B6/P2: establish identification baselines and measurement assumptions.
5. R6/R7/P7: compare solution learning, vector-field learning, and physical parameter fitting.
6. R8/R9: build a small operator-learning demonstration.
7. P3/P4: design multimachine and converter extensions.
8. B8/R11/P5: prepare uncertainty and model-updating exercises.



### 16.4 Academic and lab-building value

The course can become a shared onboarding resource for future research students: benchmark definitions, baseline implementations, reproducible failure cases, and project briefs. Keep teaching assessment distinct from research publication claims. A student project becomes a potential paper only after a specific novelty claim, adequate literature review, and stronger validation have been established.

## 17. Advanced extensions and maintenance

For a later advanced course or seminar, consider graph-based dynamic models; conservation/dissipation-aware architectures; DAE-constrained learning; event-time sensitivities; Bayesian inverse problems; multifidelity learning; active sampling near security boundaries; rigorous stability verification; and measurement-driven converter identification.

Scientific foundation models and generative approaches can be discussed as research frontiers. They should enter the assessed core only when the power-system task, baseline, data budget, and evaluation benefit are clear. Avoid replacing essential numerical and identification concepts with a catalogue of fashionable architectures.

Before each offering, check current course links, software environments, benchmark provenance, article versions, and reuse notices. Retain stable foundational readings; update a small number of advanced papers rather than rebuilding the entire syllabus annually.

**Release gate:** the course is ready when students can run the core labs, reproduce expected qualitative conclusions, understand all parameter/state definitions, identify at least one method failure, and trace reused assets to their sources.

## 18. Reference directory

The IDs below are the internal citations used throughout this report. URLs point to publisher records, official author resources, institutional pages, or repositories. Access checked or discovered on 8 October 2026; partial-access qualifications are recorded above.

### Books

- **B1.** Kundur, P., and Malik, O. P. *Power System Stability and Control*, 2nd ed. McGraw Hill. [Publisher](https://www.mheducation.com/highered/mhp/product/power-system-stability-control-second-edition.html).
- **B2.** Milano, F. (2010). *Power System Modelling and Scripting*. Springer. [DOI/publisher](https://link.springer.com/book/10.1007/978-3-642-13669-6).
- **B3.** Brunton, S. L., and Kutz, J. N. *Data-Driven Science and Engineering*. [Official companion website](https://www.databookuw.com/). Check edition alignment when assigning chapter numbers.
- **B4.** Bishop, C. M., and Bishop, H. (2024). *Deep Learning: Foundations and Concepts*. [Official website](https://www.bishopbook.com/); [publisher](https://link.springer.com/book/10.1007/978-3-031-45468-4).
- **B5.** Thuerey, N., et al. *Physics-based Deep Learning*. Online book, v0.3; originating citation 2021. [Contents](https://physicsbaseddeeplearning.org/intro.html).
- **B6.** Ljung, L. *System Identification: Theory for the User*, 2nd ed. [Publisher record](https://www.pearson.com/en-ca/subject-catalog/p/system-identification-theory-for-the-user/P200000000437).
- **B7.** Yazdani, A., and Iravani, R. (2010). *Voltage-Sourced Converters in Power Systems: Modeling, Control, and Applications*. [Wiley](https://onlinelibrary.wiley.com/doi/book/10.1002/9780470551578).
- **B8.** Särkkä, S., and Svensson, L. (2023). *Bayesian Filtering and Smoothing*, 2nd ed. [Publisher](https://www.cambridge.org/core/books/bayesian-filtering-and-smoothing/F88740E8D25010CF3119A5CA379FA37A); [author-hosted manuscript](https://users.aalto.fi/~ssarkka/pub/bfs_book_2023_online.pdf); [companion code](https://github.com/EEA-sensors/Bayesian-Filtering-and-Smoothing).
- **B9.** Brenan, K. E., Campbell, S. L., and Petzold, L. R. *Numerical Solution of Initial-Value Problems in Differential-Algebraic Equations*. [SIAM record](https://epubs.siam.org/doi/10.1137/1.9781611971224.fm).



### General SciML methods

-  **R1.** Karniadakis et al. (2021). *Physics-informed machine learning*. [Nature Reviews Physics](https://www.nature.com/articles/s42254-021-00314-5).
- **R2.** Baydin et al. *Automatic differentiation in machine learning: a survey*. [Author manuscript](https://arxiv.org/abs/1502.05767).
- **R3.** Raissi, M., Perdikaris, P., and Karniadakis, G. E. (2019). *Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations*. [JCP](https://www.sciencedirect.com/science/article/pii/S0021999118307125); [author resource](https://maziarraissi.github.io/PINNs/).
- **R4.** Wang, S., Sankaran, S., Wang, H., and Perdikaris, P. (2023). *An Expert's Guide to Training Physics-informed Neural Networks*. [Manuscript](https://arxiv.org/abs/2308.08468).
- **R5.** Krishnapriyan et al. (2021). *Characterizing possible failure modes in physics-informed neural networks*. [Manuscript](https://arxiv.org/abs/2109.01050).
- **R6.** Chen et al. (2018). *Neural Ordinary Differential Equations*. [Manuscript](https://arxiv.org/abs/1806.07366).
- **R7.** Rackauckas et al. *Universal Differential Equations for Scientific Machine Learning*. [Manuscript, 2020; revised 2021](https://arxiv.org/abs/2001.04385).
- **R8.** Lu et al. *Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators*. [Journal DOI](https://doi.org/10.1038/s42256-021-00302-5); [earlier manuscript](https://arxiv.org/abs/1910.03193).
- **R9.** Wang, S., Wang, H., and Perdikaris, P. *Learning the solution operator of parametric partial differential equations with physics-informed DeepOnets*. [Manuscript](https://arxiv.org/abs/2103.10974).
- **R10.** Kovachki et al. (2023). *Neural Operator: Learning Maps Between Function Spaces With Applications to PDEs*. [JMLR](https://jmlr.org/papers/v24/21-1524.html).
- **R11.** Psaros et al. *Uncertainty Quantification in Scientific Machine Learning: Methods, Metrics, and Comparisons*. [Manuscript](https://arxiv.org/abs/2201.07766).
- **R12.** Kopaničáková, A., and Riccietti, E. (2026). *Introduction to optimization methods for training SciML models*. [Preprint v2](https://arxiv.org/abs/2601.10222v2); [notebooks](https://github.com/kopanicakova/intro_opt_SciML).
- **R13.** Brunton, S. L., Proctor, J. L., and Kutz, J. N. *Discovering governing equations from data: Sparse identification of nonlinear dynamical systems*. [Manuscript](https://arxiv.org/abs/1509.03580).
- **R14.** Li et al. *Fourier Neural Operator for Parametric Partial Differential Equations*. [Manuscript](https://arxiv.org/abs/2010.08895).



### Power-system papers

- **P0.** Hatziargyriou et al. (2021). *Definition and Classification of Power System Stability – Revisited & Extended*. IEEE TPWRS, 36(4), 3271–3281. [DOI](https://doi.org/10.1109/TPWRS.2020.3041774); [institutional record](https://research.manchester.ac.uk/en/publications/definition-and-classification-of-power-system-stability-revisited/).
- **P1.** Misyris, G. S., Venzke, A., and Chatzivasileiadis, S. (2020). *Physics-Informed Neural Networks for Power Systems*. IEEE PES GM. [DOI](https://doi.org/10.1109/PESGM41954.2020.9282004); [manuscript](https://arxiv.org/abs/1911.03737); [code](https://github.com/gmisy/Physics-Informed-Neural-Networks-for-Power-Systems).
- **P2.** Stiasny, J., Misyris, G. S., and Chatzivasileiadis, S. (2021). *Physics-Informed Neural Networks for Non-linear System Identification for Power System Dynamics*. IEEE PowerTech. [DOI](https://doi.org/10.1109/PowerTech46648.2021.9495063); [manuscript](https://arxiv.org/abs/2004.04026).
- **P3.** Stiasny, J., Misyris, G. S., and Chatzivasileiadis, S. *Transient Stability Analysis with Physics-Informed Neural Networks*. [Manuscript v3](https://arxiv.org/abs/2106.13638v3).
- **P4.** Nellikkath, R., Murzakhanov, I., Chatzivasileiadis, S., Venzke, A., and Bakhshizadeh, M. K. (2024). *Physics-informed neural networks for phase locked loop transient stability assessment*. EPSR, 236, 110790. [DOI](https://doi.org/10.1016/j.epsr.2024.110790); [paper-linked code](https://github.com/RahulNellikkath/PINN_for_PLL_Stability_Assessment). Repository execution/access not audited.
- **P5.** Stock, S., Stiasny, J., Babazadeh, D., Becker, C., and Chatzivasileiadis, S. (2023). *Bayesian Physics-Informed Neural Networks for Robust System Identification of Power Systems*. IEEE PowerTech. [DOI](https://doi.org/10.1109/POWERTECH55446.2023.10202692); [manuscript](https://arxiv.org/abs/2212.11911).
- **P6.** *Physics-informed machine learning for power system dynamics: A framework incorporating trustworthiness* (2025). [Publisher record](https://www.sciencedirect.com/science/article/pii/S2352467725002000). Supplementary lead; full bibliographic and technical review pending.
- **P7.** Kang, S., Kim, S., and Yun, S. (2026). *Knowledge Integration in Differentiable Models: A Comparative Study of Data-Driven, Soft-Constrained, and Hard-Constrained Paradigms for Identification and Control of the Single Machine Infinite Bus System*. [Preprint v2](https://arxiv.org/abs/2602.09667v2).
- **P8.** *Physics-informed neural networks for power systems: A systematic review* (2026). [Publisher record](https://www.sciencedirect.com/science/article/pii/S2352467726001438). Supplementary lead; full text and bibliography not audited.



### Courses, tutorials, and recordings

- **C1.** JHU EN.560.652, Ján Drgoňa. [Course repository](https://github.com/drgona/SciML-Course).
- **C2.** Beckers, Nghiem, and Drgoňa. L4DC 2026 *Scientific Machine Learning for Modeling, Optimization, and Control*. [Website](https://sciml-l4dc2026.github.io/SciML-L4DC2026/); [repository](https://github.com/SciML-L4DC2026/SciML-L4DC2026).
- **C3.** MIT *Parallel Computing and Scientific Machine Learning*. [Book/notes](https://book.sciml.ai/); [course](https://book.sciml.ai/course/); [lectures](https://book.sciml.ai/lectures/).
- **C4.** Illinois CS/ME 598 SML, Spring 2026. [Syllabus/materials](https://github.com/598sml/598sml-s26-syllabus).
- **C5.** ETH *AI in the Sciences and Engineering*. [HS2026 page](https://camlab-ethz.github.io/ai4s-course/); [Fall 2025 archive](https://camlab-ethz.github.io/ai4s-course/fall2025/); [DLSC 2023](https://camlab.ethz.ch/teaching/deep-learning-in-scientific-computing-2023.html).
- **C6.** iAI KAIST *Scientific Machine Learning*. [Course and reuse statement](https://iailab.kaist.ac.kr/teaching/scientific-machine-learning).
- **C7.** University of Washington *Physics Informed Machine Learning Workshop* (2019). [Organizer page](https://www.databookuw.com/seminars/page-22/).
- **C8.** IIT Bombay/NPTEL *Power System Dynamics and Control*. [Course](https://nptel.ac.in/courses/108101004); [archived syllabus](https://archive.nptel.ac.in/content/syllabus_pdf/108101004.pdf).
- **C9.** IIT Kharagpur/NPTEL *Power System Dynamics, Control and Monitoring*. [Course](https://nptel.ac.in/courses/108105133); [syllabus](https://archive.nptel.ac.in/content/syllabus_pdf/108105133.pdf).
- **C10.** Oxford *Physics Informed Neural Networks*, 2025–2026. [Official page](https://algo.cs.ox.ac.uk/teaching/courses/2025-2026/pinn/index.html).
- **C11.** IEEE PES *Physics-informed Machine Learning for Power Systems*. [Webinar slide-resource listing](https://resourcecenter.ieee.org/education/webinars/pes_ed_web_mlps_102224_sld).
- **C12.** Spyros Chatzivasileiadis. [Teaching-resource page](https://www.chatziva.com/teaching.html).
- **C13.** PSCC 2024 tutorial resources. [Program/landing page](https://www.chatziva.com/pscc2024.html); [indexed author-hosted slide deck](https://www.chatziva.com/PSCC2024Tutorial/3_PSCC2024_Tutorial_Spyros.pdf). Partial-access lead; full asset review pending.



### Software and permissions

- **S1.** ANDES. [Official repository](https://github.com/CURENT/andes); [documentation](https://docs.andes.app/en/stable/); [time-domain tutorial](https://docs.andes.app/en/stable/tutorials/04-time-domain.html).
- **S2.** torchdiffeq. [Official repository](https://github.com/rtqichen/torchdiffeq).
- **S3.** DeepXDE. [Official repository](https://github.com/lululxvi/deepxde).
- **S4.** NeuroMANCER. [Official repository](https://github.com/pnnl/neuromancer). Linked by L4DC; package-level audit not performed here.
- **S5.** Dynamics Lab. *Data-Driven Science and Engineering — Python companion notebooks*. [Repository](https://github.com/dynamicslab/databook_python). Repository description checked; execution and asset-specific reuse terms not audited.
- **L1.** Creative Commons. [License descriptions](https://creativecommons.org/cc-licenses/).
- **L2.** NPTEL. [Current site](https://nptel.ac.in/); [archived license notice](https://archive.nptel.ac.in/footer.html). Resolve differing notices at the individual-asset level.

---

**First development decision:** freeze the SMIB equations, observation model, and CCT definition, then implement the reference simulator and five laboratory briefs. Those decisions make the larger syllabus concrete and keep the three application categories scientifically connected.