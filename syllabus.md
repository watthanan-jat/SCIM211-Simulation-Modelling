# SCIM211 Simulation Modelling

## Course Syllabus: Semester 1, Academic Year 2026


## 1. Course Information

| Item | Details |
|---|---|
| Course code | SCIM211 |
| English title | Simulation Modelling |
| Thai title | วทคอ ๒๑๑ การจำลองเลียนแบบ |
| Credits | 3 (3-0-6) |
| Programme | Bachelor of Science Programme in Industrial Mathematics and Data Science, International Programme |
| Course type | Compulsory course |
| Semester and level | Semester 1, Class Level 2 |
| Expected class size | Approximately 30 students |
| Prerequisite | SCIM121 Statistical Data Analysis I |
| Co-requisite | None |
| Latest course-specification revision | 10 June 2026 |

The official credit structure is 3 hours of theory and 6 hours of self-study per week. 


## 2. Instructor

**Asst. Prof. Dr. Watthanan Jatuviriyapornchai (WJ)**<br>
B203/8 Department of Mathematics, Faculty of Science, Mahidol University, Bangkok <br>
Telephone: 02-201-5356<br>
Email: [watthanan.jat@mahidol.ac.th](mailto:watthanan.jat@mahidol.ac.th)

The instructor is both the course coordinator and course-responsible instructor. 
Lab assistants will support designated lab and project sessions.

## 3. Course Goals

The course introduces the fundamental principles and applications of simulation modelling as a tool for analysing complex systems. It develops the theoretical and practical skills required to design, implement, run, and analyse simulation models.

By connecting simulation to mathematics and data science, the course prepares students to:
- represent a real system as a model;
- generate and control random behaviour;
- implement Monte Carlo and discrete-event simulations;
- analyse simulation inputs and outputs statistically;
- evaluate model credibility through verification and validation; and
- use simulation evidence to compare alternatives and support decisions.

## 4. Course Description

The importance of simulation; example models; generating random numbers; simulating random variables; Monte Carlo simulation; modelling inputs; analysing outputs; Markov chains and discrete events; discrete-event simulation; variance reduction techniques; model validation; and computer techniques for simulation.

## 5. Course-Level Learning Outcomes

On completion of the course, students will be able to:

1. **CLO1 — Explain:** Explain the fundamental concepts and importance of simulation modelling in solving complex problems.
2. **CLO2 — Generate:** Generate random numbers and random variates from specified probability distributions using standard computational techniques.
3. **CLO3 — Implement:** Implement Monte Carlo simulation methods and discrete-event models to solve problems in different application domains.
4. **CLO4 — Analyse:** Analyse simulation inputs and outputs using appropriate statistical techniques to create accurate model representations and draw valid conclusions.
5. **CLO5 — Construct:** Construct Markov chain models to represent stochastic processes in real-world systems.
6. **CLO6 — Evaluate:** Evaluate simulation models through systematic validation approaches and appropriate tools for different problem domains.

## 6. Learning and Teaching Approach

The course combines:
- interactive lectures and guided discussion;
- worked examples and short exercises;
- experience-based case studies;
- Python demonstrations and guided notebook work;
- hands-on lab investigations;
- scenario comparison and statistical interpretation;
- group project work; and
- questions and oral explanations used to check individual understanding.

The continuing context is a **Coffee Shop Simulation Project**. Each lab adds a new capability to the same model: system definition, random-number generation, random variables, Monte Carlo analysis, discrete-event queues, Markov-chain loyalty, output analysis, and validation.

## 7. Assessment

| Assessment | Weight | Key information |
|---|---:|---|
| Midterm examination | 25% | Individual 3-hour written examination |
| Final examination | 25% | Individual 3-hour written examination |
| Lab exercises | 21% | 7 assessed hands-on lab sessions |
| Quizzes | 20% | Four quizzes offered; best two scores count |
| Group Mini Project | 9% | Group simulation project and Week 16 Project Challenge |
| **Total** | **100%** |  |

Assessment is designed to measure conceptual understanding, computational skills, statistical reasoning, model construction, validation, and communication. Students may be asked to explain their work orally as part of the assessment of understanding.

### 7.1 Examination Policy

The examination component is worth 50% in total:
- Midterm examination: 25%
- Final examination: 25%

There is no re-examination offered as part of this course. University and Faculty regulations apply to all examinations and requests based on exceptional circumstances.

### 7.2 Lab Exercise Policy

Seven lab exercises contribute 21% of the final grade.
- Attendance is compulsory and will be monitored.
- If you cannot attend a lab, inform the instructor in advance.
- Each lab contains several required exercises. Complete all exercises to be eligible for full marks.
- During assessment, you may be asked questions to demonstrate that you understand the problem, your code, and your solution.
- Marks may be withheld when a student cannot explain the submitted work.
- The instructor and lab assistants will help you think through problems, but they will not write or debug programs for you.
- AI tools may be used as learning aids during lab sessions, but students remain fully responsible for checking, understanding, and explaining all AI-assisted work.
- Copying or submitting AI-generated code, answers, or explanations without understanding them is irresponsible AI use.
- **A student who cannot demonstrate an understanding of AI-assisted work will receive a score of 0 for that lab.**
- Submit work during the scheduled lab session whenever possible.
- Work for Lab *n* may also be submitted before noon (12:00) at the following lab session, Lab *n+1*. No marks will be awarded after that deadline.
- A missed lab requires a valid reason. Medical absence requires supporting medical documentation.
- Students remain responsible for making up missed learning activities in their own time.

#### Lab Scoring Guide

| Score | Description |
|---:|---|
| 0 | Absent or completes less than 50% of the exercises |
| 1 | Completes at least 50% of the exercises |
| 2 | Completes all exercises |
| 3 | Completes all exercises and answers questions promptly |

### 7.3 Quiz Policy

Four quizzes will be held during lecture sessions in **Weeks 5, 7, 13, and 17**.

- Only the best two quiz scores count toward the final grade
- The two counted quizzes contribute 20% in total.
- There are no replacement quizzes under any circumstances.
- Because the best two of four scores are used, students are responsible for attending at least two quiz sessions during the semester.

### 7.4 Group Mini Project and Project Challenge

The Mini Project is worth 9% and is completed in groups.

Throughout the semester, each group will build a reusable coffee-shop simulation model. The model should allow the group to change inputs such as arrival rates, service times, demand, staffing, or operating policies without rewriting the entire program.

In Week 16, each group will receive an assigned **Project Challenge**. The group must apply the model it has built, run appropriate experiments, interpret uncertainty, and support a practical recommendation with evidence. The detailed project outline will be released later in the course.

## 8. Course Timetable

Regular sessions are scheduled for **10:00–12:00**. Tuesday sessions focus on theory, modelling, and guided activities. Designated Wednesday sessions are used for labs or the Project Challenge.

| Week | Date | Topic or activity |
|---:|---|---|
| 1 | Tue 4 Aug | Introduction; why simulate; course journey; coffee-shop running example |
| 2 | Tue 11 Aug | System concepts: entities, resources, attributes, activities, events, and state variables |
| 2 | Wed 12 Aug | **Lab 1:** From Real System to Simulation Model |
| 3 | Tue 18 Aug | Probability review: random variables, distributions, expectation, variance, and sampling ideas |
| 4 | Tue 25 Aug | Random-number generation: pseudo-random numbers, seeds, linear congruential generators, and periods |
| 4 | Wed 26 Aug | **Lab 2:** Can Computers Really Be Random? |
| 5 | Tue 1 Sep | Simulating random variables I: inverse transform and discrete random-variable simulation; **Quiz 1** |
| 6 | Tue 8 Sep | Simulating random variables II: accept–reject ideas, exponential service times, and input generation |
| 6 | Wed 9 Sep | **Lab 3:** From Random Numbers to Random Variables |
| 7 | Tue 15 Sep | Monte Carlo I: repeated random experiments, expected values, probabilities, and sampling error; **Quiz 2** |
| 8 | Tue 22 Sep | Monte Carlo II: confidence intervals, integration, decision comparison, and profit simulation |
| 8 | Wed 23 Sep | **Lab 4:** Monte Carlo Profit and Promotion Decision |
| 9 | 28 Sep–2 Oct | **Midterm week:** no regular class |
| 10 | Tue 6 Oct | Discrete-event simulation I: event scheduling, event lists, queues, arrivals, departures, and server state |
| 10 | Wed 7 Oct | **Lab 5:** Discrete-Event Simulation of a Coffee Shop Queue |
| 11 | Tue 13 Oct | Discrete-event simulation II: replications, queue performance, and scenario comparison |
| 12 | Tue 20 Oct | Markov chains I: states, transition matrices, and one-step and multi-step transitions |
| 12 | Wed 21 Oct | **Lab 6:** Markov Chains and Customer Loyalty |
| 13 | Tue 27 Oct | Markov chains II: long-run behaviour, stationary distributions, and interpretation; **Quiz 3** |
| 14 | Tue 3 Nov | Input/output analysis: input data, distribution fitting, replications, and confidence intervals |
| 14 | Wed 4 Nov | **Lab 7:** Validation and Final Recommendation |
| 15 | Tue 10 Nov | Variance reduction and validation; project wrap-up |
| 16 | Tue 17 Nov | Project Challenge briefing and group model application |
| 16 | Wed 18 Nov | **Project Challenge session:** group work and submission |
| 17 | Tue 24 Nov | Course review; **Quiz 4** |
| — | To be announced | Final examination |

The timetable may be adjusted when required by the University calendar. Any approved change will be announced through the course communication channel.

## 9. Grading

Performance is evaluated according to Faculty of Science and Mahidol University regulations.

| Score | Letter grade |
|---:|:---:|
| 85–100 | A |
| 75–84 | B+ |
| 70–74 | B |
| 65–69 | C+ |
| 60–64 | C |
| 55–59 | D+ |
| 45–54 | D |
| 0–44 | F |

## 10. Required and Suggested Resources


### Course Materials

Lecture materials, lab sheets, starter notebooks, data, and released exercises are provided through the course repository:

[SCIM211 Simulation Modelling repository](https://github.com/watthanan-jat/SCIM211-Simulation-Modelling)

Lecture notes will be posted in the course Google Classroom.

Students should retain an organised copy of their notebooks, code, data, results, and feedback because later labs and the Mini Project build on earlier work.

### Suggested Texts

1. Ross, S. M. *Simulation*.
2. Law, A. M. *Simulation Modeling and Analysis*.
3. Banks, J., Carson, J. S. II, Nelson, B. L., Nicol, D. M., and Shahabudeen, P. *Discrete-Event System Simulation*.

   
## 11. Communication, Conduct, and Responsible Work

- Google Classroom is the official channel for class communication, announcements, and submission of assessed work.
- Ask questions during lectures and labs; discussion is part of the learning process.
- Submit work that you understand and can explain.
- AI may support your learning, but it may not replace your own reasoning, modelling decisions, or understanding.
- Follow Faculty and University rules for assessment, academic integrity, attendance, and evidence for absence.
- Use course data and computing resources responsibly.
- Follow the course [Academic Integrity and AI Policy](ai_policy.md) when using references, generative AI, or coding assistants.
- Check course announcements regularly for approved updates to dates, rooms, or assessment arrangements.

## 12. Student Questions and Appeals

Questions about course content, assessment, or feedback should first be discussed with the instructor.

Formal appeals may be submitted to:

**Educational Affairs Division**<br>
Faculty of Science, Mahidol University<br>
3rd Floor, MUSES Building<br>
272 Rama VI Road, Ratchathewi District<br>
Bangkok 10400, Thailand<br>

## 13. Course Evaluation and Improvement

The course is reviewed using:
- student evaluation of the instructor;
- course evaluation;
- student learning records and achievement of the CLOs; and
- instructor reflection on course delivery.

Student needs and feedback will be considered when revising future course delivery. Achievement of the course learning outcomes will be reviewed using evidence from the summative assessments.
