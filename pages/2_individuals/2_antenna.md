---
title: Ku Antenna
parent: Work Area
nav_order: 2
permalink: /kuantenna/

--- 

<div style="display:flex">
  <img src="{{site.baseurl}}/assets/images/profiles/jg.jpg" alt="Hang Jin Guang" width="200" style="border-radius:50%">
  <div style="margin-left: 20px">
    <h2>Ku Antenna</h2>
  </div>
</div>


# **1\.**  **Introduction**

Problem: No space-based Ku antenna that can be directly procured in the frequency range of 13.93-13.99GHz.

Objective & Scope: To design, prototype and test an antenna operating in the required frequency range of 13.93-13.99GHz for space-based application. 

Novelty: Addresses the gap in existing commercially-available space-based Ku-band antennae.

Specifications:

·       Frequency range: 13.95 \+- 0.3 GHz

·       Maximum size: 53mm x 57 mm x 4.26 mm (accounting for mounting holes)

·       Minimum gain: 10dBi

·       Minimum beamwidth: 24 deg

 

## **1.1**  **Background and Motivation**

***¨ Compelling articulation of the project’s novelty and/or value proposition.***

 

## **1.2**  **Problem Statement**

***What problem are you trying to address in your project? What are you trying to achieve?***

## **1.3**  **Objectives and Scope**

***What are you trying to achieve?***

***Objective and scope of the project are clearly defined and feasible.***

## **1.4 Specifications and Constraints**

***¨ Design specifications are clearly presented, well justified, and coherent the intended deliverables of the project.***

## **1.5 Novelty and Contributions**

***How is your project different from existing or past work?¨***

 ***Compelling articulation of the project’s novelty and/or value proposition.***

# **2\. Background and Literature Review**

## **2.1**  **Growth of High-Frequency CubeSat Communications**

***What is the setting of the problem you are trying to address? Where is your project situated within the bigger scheme of things?:***

Problem Setting

·       With the growing demand for satellite communication, lower frequency bands like C and S are becoming saturated, prompting a shift to higher bands like Ku and Ka for faster, high data rate communication and wider bandwidth (Gurbet & Dogu, 2025).

High cost and complexity? Why is it not commercially available?

To

Info about diff types of cubesat antennae: Planar, planar arrays, reflector,

·        

***Comprehensive and detailed discussion about the context of the problem using information gathered from an extensive range of relevant, authoritative, and up-to-date sources.***

## **2.2 Existing CubeSat Antenna Technologies**

Planar antennas

Planar arrays

Reflectors & deployables

## **2.3 Why Ku-Band (13.93–13.99 GHz) Is Challenging**

## **2.4 Limitations of Commercial Space-Qualified Ku Antennas**

## **2.5 Summary of Gaps in Existing Work**

 

***3&4) How do you intend to achieve the intended deliverables of your project? How do you know that your approach is suitable? Chosen methodologies/concept solutions and their alternatives are evaluated in a systematic and comprehensive manner.***

# **3\. Design Methodology**

## **3.1 Key Antenna Performance Metrics**

Key antenna metrics

·       S11 or Reflection coefficient: the ratio of the reflected voltage amplitude against the source voltage amplitude. It is a measure of how much the signal gets reflected due to impedance mismatches (for RF, the standard source impedance is 50 Ohms, so the antenna is also expected to be at 50 Ohms).

`o`   The impendance bandwidth is the frequency range for which the S11 is \-10dB or less.  Thus minimally from 13.92 to 13.98 GHz, the S11 must be \<-10dB.

`o`   For the center frequency of 13.95GHz, generally \-20dB or less is expected (DSO)

·       Polarisation: To lessen losses from polarization mismatch, CubeSat antennae typically employ circular polarization (CP). (Gurbet & Dogu, 2025).

`o`   There are 2 types of CP: RHCP and LHCP.

`o`   Polarisation of the ground and space antenna will have to match.

`o`   The polarisation was initially fixed at right-hand circular polarization.

·       Gain and Beamwidth: The peak gain will have to be \>=10dBi and the half-power beamwidth must be at \+-12 degrees from the center.

·       Axial ratio: Measures how circularly polarized the antenna is. A high axial ratio means the beam is elliptically polarized. When AR is very high, the beam is no different from linear polarization. \<3dB (2 times) is ideal.

## **3.2 Selection of antenna type**

### **3.2.1 Antenna type evaluation**

| Antenna Type | Description / Structure | Advantages | Disadvantages | Typical Use / Notes ff |
| ----- | ----- | ----- | ----- | ----- |
| Planar (Patch / Slot) | Flat microstrip or slot radiators integrated on CubeSat body | • Compact and low profile • Lightweight, easy to integrate • No deployment needed • Low cost and simple fabrication | • Low gain (\~5–10 dBi) • Narrow bandwidth • Susceptible to detuning from CubeSat structure | Common for low-power or short-range missions (e.g., telemetry, inter-satellite links) |
| Planar Array (Phased / Transmitarray / Leaky-Wave) | Array of planar elements (patches, SIW, or slots), sometimes reconfigurable | • Higher gain (15–25 dBi) • Beam steering possible • Good bandwidth • Fully planar—can fit CubeSat face | • Increased feed and control complexity • Higher power consumption • Limited aperture due to CubeSat face size | Suited for high-data-rate Ka/K-band missions; reconfigurable phased arrays achieve up to 22 dBi |

·       Given size constraints, only planar antennae can meet this criteria

`o`   Planar antennae, as its name suggests, fit in a 2d plane

### **3.2.2 Selection of Patch Antenna**

·       The most common type of planar antenna is the microstrip patch antenna (or just called patch antenna).

`o`   This is how a rectangular linearly polarized patch antenna works:

`o`   It consists of a conducting patch layered on top of a dielectric substrate, which is on top of a conductive ground plane

`o`   It can be easily manufactured via PCB manufacturing.

`o`   Through a feedline, alternating E fields are formed between the patch and ground plane, which resonate and escape through both ends of the patch antenna (radiating slots)

`o`    ![Diagram of a diagram of a patchAI-generated content may be incorrect.][image1] (top and bottom draw ellipses)

`o`   [https://www.geeksforgeeks.org/microstrip-patch-antenna/](https://www.geeksforgeeks.org/microstrip-patch-antenna/)

`o`   For a circular polarized patch antenna, the basic operating principle in which the E fields escape from the gaps between the patch and the ground plane is the same. I will explain later how it is modified to achieve CP.

·       Planar antennas, especially patch antennae, have been frequently employed for satellite communication in single-element and array arrangements due to their small physical area in CubeSats. However, planar antennae can have low gain and narrow bandwidths. Fortunately, for high frequencies such as Ku, the size of one element is small, which allows arrays to be created for the gain to be increased.

·       The choice of patch antenna was clear from the start, with it being recommended by both my NUS and DSO mentors.

`o`   Circularly polarised patch antennae are widely studied and used, with many formulae available to aid in its design. (Balanis C. A., 2005\)

`o`   While other forms of planar antennae such as slot antennae are more rarely used, with more complex modifications required for circular polarization. ([dergipark.org.tr/en/download/article-file/270740](https://dergipark.org.tr/en/download/article-file/270740))

### **3.2.3 Preliminary feasibility calculations**

·       Preliminary calculations to support the feasibility of patch antenna:

`o`   Preliminary estimates utilizing the formula for size of a rectangular patch antenna estimates that a singular Ku element would be the size 7mm x 5.2mm. ([Microstrip Patch Antenna Calculator](https://www.pasternack.com/t-calculator-microstrip-ant.aspx)) One element can achieve around \~3-4dBi. To reach \>10dBi, we can double the element 1 element: 3dBi, 2 elements: 6dBi, 4 elements 9 dBi, 8 elements: 12 dBi. With a half wavelength (\~10.8mm) between each element, and considering a 2x4 array, the patches will only take up \~37mm by 18mm. \~0.3 wavelength extension on every side adds \~7mm of ground plane gives 44mm by 21mm which just nice fits within the 53mm x 57mm requirement.

`o`   Hence a microstrip patch array is a viable solution given our specifications.

## **3.3 Selection of type of patch antenna**

·       Types: Circular, Truncated square patch, Dual feed patch with wilkinson power divider

`o`   Truncated square patch is eliminated because of its low gain (according to DSO mentor, [Truncated microstrip square patch array antenna 2 × 2 elements with circular polarization for S-band microwave frequency | IEEE Conference Publication | IEEE Xplore](https://ieeexplore.ieee.org/document/8240384))

`o`   Dual-fed rectangular patch with wilkinson power divider

`o`   Circular probe-fed antenna (suggested by NUS mentor)

`o`   Comparing the dual-fed patch with the circular patch, a quick analysis reveals that the WPD is more complicated as it requires a feed network to split the power into two feeds for the antenna, while the circular antenna only requires 1 feed to achieve RHCP.

`o`   Thus I chose the circular antenna due to the absence of the feed network needed.

**Analytical Design Calculations (Patch size, spacing, bandwidth, etc.)**

## **3.4 Design Software**

Choice of HFSS

## ---

***\-What have you created to achieve the intended deliverables of your project? What are the purposes of these specimens or prototypes? How did you create these specimens or prototypes? Multiple prototypes/specimens are thoughtfully created with extensive references to and sound application of knowledge/principles/theories in relevant fields. There is clear evidence of fine workmanship in the prototypes/specimens made.***

***\-What have you found out through the specimens or prototypes which you have created and/or tests which you have conducted in your project? How do you know that your findings are valid?*** In-depth analysis/explanation of data and observations is performed through precise use of appropriate methods, techniques, theories, and/or concepts to demonstrate or explain key behavior/trends.

 

# **4\.**  **Prototype Development**

Included for each prototype:

5\. Simulation Results and Analysis

5.1 S11 Performance

5.2 Realized RHCP Gain & Beamwidth

5.3 Axial Ratio Across Beam

5.4 Effect of Key Parameters (Rp, Sf, stubs, feed design)

5.5 Comparison of Design Variants

 

## **4.1 Prototype 1: Dual-Feed Patch with Wilkinson Divider**

Design

Purpose

Key learnings

·       Created the patch with dimensions according to the paper’s formulae.

·       Copied the power divider network without modification

·       Purpose: To learn basic skills in HFSS: creating patch, testing for results: S11, gain, axial ratio.

·       Reflection:

`o`   Learnt that further tuning of the feed network is required to achieve a 90 degree phase shift. Hence it is not as easy as just copying a design from online.

`o`   S11, and axial ratio measurements were correct. But I then learnt that I am not supposed to take total gain, but the realisedRHCPgain. (it’s likely that the first takes the maximum gain obtained from all possible polarisations which is not what we want).

 

## **4.2 Prototype 2: Circular Patch Element**

Stub study

Feed offset tuning

AR and S11 performance

Circular patch

·       Investigation of effect of side stubs

`o`   (axial ratio, gain, hpbw, s11)

`o`   Singular patch (no stubs) has very bad axial ratio of \~50-60

`o`   Singular patch (with stubs):

`o`   Array with stubs (holes in a ‘square’):

`o`   Array without stubs (holes in a ‘square’)

·       Investigation of type of feed:

`o`   sequentially rotated arc feed network vs right-angled

`o`   Assess the difficulty level in creating this arc network à eventually realized the complexity in tuning. The parameters for circular arcs are difficult to set as it can be hard to set the centre

`o`   hence decided to go for right-angled feed network

·       Investigation of effect of changing Rp and Sf on S11, axial ratio, hpbw, axial ratio, gain)

`o`   Increasing Rp generally decreases the resonant frequency

·       Investigation of rotating vs not rotating patches in 2x2 array (S11, axial ratio, hpbw, gain)

`o`   No stubs:

§  With rotating (holes in a ‘square’): 0.6863 dB

§  No rotating

`o`   Stubs:

§  With rotating

§  No rotating

 

## **4.3 Prototype 3: 2×2 Circular Patch Array**

Rotation vs non-rotation

Feed network design

Array behaviour (coupling, HPBW, gain)

## **4.4 Final Manufacture-Ready Design**

##  

# **5\.**  **Testing Methodology**

***\-What tests have you performed to investigate the key questions in your project? What are the purposes of these tests? How did you conduct these tests? Intended purposes/scope of testing are clearly defined, and testing of prototypes/specimens is conducted conscientiously using the best possible approaches for the intended purposes.***

***\-What have you found out through the specimens or prototypes which you have created and/or tests which you have conducted in your project? How do you know that your findings are valid?*** In-depth analysis/explanation of data and observations is performed through precise use of appropriate methods, techniques, theories, and/or concepts to demonstrate or explain key behavior/trends.

## **5.1 Simulation Testing**

**A brief summary of the tests done during prototyping**

As mentioned before, there are 3 key metrics that need to be tested in simulation to evaluate if the antenna design meets the required specifications.

·       S11

·       Gain (realized RHCP gain), Half-power beamwidth

·       Axial Ratio

 

# **5.1 Post Fabrication Tests**

Tests after the antenna array is manufactured

S11: A Vector Network Analyzer (VNA) will be connected to the single source coax connector (likely SMA) (refer to Fig XX.), to determine the S11 in the desired bandwidth of 13.95 \+- 0.03 GHz.

Gain, HPBW, Radiation pattern: Anechoic chamber

Axial ratio: Anechoic chamber

## **5.1 S11 Measurement (VNA Setup)**

## **5.2 Radiation Pattern & Gain Measurement (Anechoic Chamber)**

## **5.3 Axial Ratio Measurement**

## **5.4 Test Setup, Calibration, and Procedures**

## ---

# **6\. Expected Results and Validation Plan**

(If you will only test after W1)

## **6.1 Simulated vs Expected Real-World Performance**

## **6.2 Sources of Discrepancy (Substrate tolerance, SMA transition, fabrication error)**

## **6.3 Plan for Model Tuning After Measurement**

## **6.4 Criteria for Success**

##  

# **6\.**  **Discussion of Progress Toward Deliverables**

***\-How well has your work addressed the intended deliverables of your project?*** Able to demonstrate that work done has excellent potential in meeting all the intended deliverables of the project.

…

 

## **7.1 Summary of Achievements**

## **7.2 Remaining Gaps**

## **7.3 Impact of Findings on Final Manufacturing**

##  

# **8\. Current Shortcomings and Improvement Plan**

***\-What are the current shortcomings in your work? How do you plan to resolve them?** Major shortcomings of work done are clearly identified, with sound and well justified proposals to resolve these shortcomings.*

 

·       Better documentation from the beginning with the labelling of HFSS files.

 

## **8.1 Shortcomings Identified**

## **8.2 Proposed Solutions and Design Refinements**

## **8.3 Risk Mitigation Strategies**

##  

# **9\. Detailed Project Completion Plan**

***\-What do you intend to do in order to ensure that you would be able to complete your project successfully?** Able to propose detailed and viable plans for completing the project, with well-articulated steps and clearly identified milestones to be reached.*

| Date | Plan |
| :---- | :---- |
| W13 (up to interim report submission) | Focus on improving report based on key points to investigate |
| Reading week – Exam week 1 | *Focus on exams* |
| 3-12 Dec | ·       Simulate section C1, C2 of feed network ·       Simulate entire feed network (schematic version) ·       Layout feed network with patches and simulate |
| 14-21 Dec | ·       Add in final SMA connector ·       Make last adjustments and preparations required for manufacturing ·       Send out design to PCB manufacturer by end of this week ·       Make arrangements for antenna testing in W1 |
| W1 (11-16 Jan) | ·       Verify S11 with VNA ·       Full chamber measurements of antenna |
| **W2–3 (18–31 Jan)** | ·       Compare measured S₁₁ and pattern vs simulation.• Identify discrepancy sources (substrate tolerance, connector mismatch, fabrication error).• Re-simulate with measured substrate thickness and εᵣ.• Tune model to align with measurements. |
| **W4–5 (1–14 Feb)** | ·       Compare measured S₁₁ and pattern vs simulation.• Identify discrepancy sources (substrate tolerance, connector mismatch, fabrication error).• Re-simulate with measured substrate thickness and εᵣ.• Tune model to align with measurements. |
| **W6–Reading (17–28 Feb)** | ·       Submit revised PCB (if necessary).• Conduct VNA \+ anechoic chamber retest.• Document performance comparison between v1 and v2. |
| **W7-8 (3–16 Mar)** | ·       Thermal and vibration tolerance study (simulation level unless you’re part of actual flight payload).• Outgas-safe material review (Rogers datasheet, soldermask, adhesives).• Write section on “space qualification considerations” for report. |
| **W9 (17–23 Mar)** | ·       Interface study: SMA-to-coax routing inside satellite.• Verify mechanical envelope fits 80 × 80 mm spec.• Coordinate with bus team for mounting and RF chain (LNA, cables). |
| **W10-11 (24 Mar – 6 Apr)** | ·       • Compile design iterations, measurement results, lessons learned.• Produce figures (S₁₁, AR, gain, radiation pattern comparisons).• Write final report sections. |
| **W12 (7–13 Apr)** | ·       • Prepare slides & poster.• Summarize key achievements: freq range 13.93–13.99 GHz, gain, axial ratio, fabrication results. |

 

 

## **9.1 Simulation & Fabrication Timeline**

## **9.2 Testing & Validation Timeline**

## **9.3 Reporting & Space Qualification Sections**

## **9.4 Final Deliverables**

##  

# **10\. Conclusion**

## **10.1 Summary**

## **10.2 Contributions**

## **10.3 Future Work ** 

[image1]: <data:image/png;base64,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>