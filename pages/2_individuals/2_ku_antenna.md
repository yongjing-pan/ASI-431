---
title: Ku Antenna
nav_order: 2
permalink: /ku_antenna/
has_toc: false
---

<div style="display:flex">
  <img src="{{site.baseurl}}/Assets/images/profiles/yj.png" alt="Pan Yongjing" width="200" style="border-radius:50%">
  <div style="margin-left: 20px">
    <h2>Pan Yongjing</h2>
    <h3>Year 4 Electrical Engineering</h3>
    <h3>A0257283X</h3>
  </div>
</div>
  
# **Contents page** {#contents-page}

[**Contents page	1**](#contents-page)

[**1\.  Introduction	1**](#1--introduction)

[1.2  Problem Statement	1](#12--problem-statement)

[1.3  Objectives and Scope	2](#13--objectives-and-scope)

[1.4 Specifications and Constraints	2](#14-specifications-and-constraints)

[1.5 Novelty and Contributions	3](#15-novelty-and-contributions)

[**2\. Background and Literature Review	3**](#2-background-and-literature-review)

[2.1 Existing CubeSat Antenna Designs	3](#21-existing-cubesat-antenna-designs)

[**3\. Design Methodology	3**](#3-design-methodology)

[3.1 Key Antenna Performance Metrics	3](#31-key-antenna-performance-metrics)

[3.2 Selection of antenna type	4](#32-selection-of-antenna-type)

[3.2.1 Concept evaluation matrix	4](#321-concept-evaluation-matrix)

[3.2.2 Mitigating the Disadvantages of Patch Antenna	5](#322-mitigating-the-disadvantages-of-patch-antenna)

[3.2.3 About the Patch Antenna	5](#323-about-the-patch-antenna)

[3.2.4. Preliminary feasibility calculations	6](#324-preliminary-feasibility-calculations)

[3.3 Selection of type of patch antenna	6](#33-selection-of-type-of-patch-antenna)

[3.4 Antenna Design Software	8](#34-antenna-design-software)

[4.1 Prototype 1: Single Patch Simulation	8](#41-prototype-1-single-patch-simulation)

[4.2 Prototype 2: 2x2 Array Simulation	10](#42-prototype-2-2x2-array-simulation)

[4.3 Prototype 3: Optimising single patch	12](#43-prototype-3-optimising-single-patch)

[4.4 Prototype 4: Optimising 2x2 array	14](#44-prototype-4-optimising-2x2-array)

[4.5 Prototype 5: Repositioning feed points	15](#45-prototype-5-repositioning-feed-points)

[4.6 Prototype 6: 2x4 Array Simulation	18](#46-prototype-6-2x4-array-simulation)

[4.7 Prototype 7: Feed network investigation	20](#47-prototype-7-feed-network-investigation)

[**5. Current Shortcomings	21**](#5-current-shortcomings)

[**6. Detailed Project Completion Plan	22**](#6-detailed-project-completion-plan)

[**7. Conclusion	24**](#7-conclusion)

[**8. References	24**](#8-references)

# **1\.  Introduction** 

This project focuses on developing a custom space-based Ku-band antenna for the Galassia 5 (G5)’s unique requirements.

## **1.2  Problem Statement**

As mentioned in the introduction to G5, the team discovered that there is no existing commercial space-qualified Ku-band communication hardware meeting our frequency requirements (13.93-13.99 GHz). The space-based Ku antenna is one crucial part of the system that together with the Ku-band upconverter and ground station, form the custom-designed communication link from the satellite to the ground station. Specifically, the antenna serves to amplify and transmit signals from the satellite to the ground station. Hence, there is a need to develop a custom Ku antenna meeting the G5 mission requirements.

## **1.3  Objectives and Scope**

To design, prototype and test an antenna operating in the required frequency range of 13.93-13.99GHz for space-based application. 

## **1.4 Specifications and Constraints**

* Frequency range: 13.95 \+- 0.3 GHz  
* Maximum size: 100mm x 100mm x 4.26 mm  
* Mounting screws separation: 63.6mm x 67.1mm  
* Minimum gain: 10dBi  
* Minimum beamwidth: 24 degrees

Besides the required frequency range, the other specifications of gain and beamwidth are designed by the team lead and system engineer according to link budget calculations. From discussions with the mechanical team, the mounting of the antenna was determined to be on a 1U (10cmx10cm) face of the CubeSat, the same configuration as Gomspace’s S-band antenna (Fig. 1\) achieving a similar gain of 7-8 dBi. Note that although the ANT2150 is actually 80mm x 80mm (rounded square in Fig. 1), our antenna can be bigger as long as it still fits on a 1U face.

![][image1]

Fig. 1: Gomspace S-band antenna ANT2150 mounting configuration. 

## **1.5 Novelty and Contributions**

As mentioned in G5’s introduction, existing communication systems do not operate in the narrow and specific frequency range of 13.93-13.99 GHz. The design of a custom Ku antenna to meet our mission’s requirements hence addresses this gap in existing commercially-available space-based Ku-band antennae.

# **2\. Background and Literature Review**

What is the setting of the problem you are trying to address? Where is your project situated within the bigger scheme of things?:Comprehensive and detailed discussion about the context of the problem using information gathered from an extensive range of relevant, authoritative, and up-to-date sources.

## **2.1 Existing CubeSat Antenna Designs**

There are many antenna designs used in CubeSats for the Ku, K and Ka bands. One review paper analyses roughly \~12 antenna designs used in recent years \[1\]. Reviewing all of them, only planar antenna types like patch and slot antennae fit our small and flat (thickness \<4.6mm) geometry requirements. Corroborating with existing missions, planar antennas, especially microstrip patches, are widely used in satellite communications due to their compact size, low profile, and ease of integration on CubeSats \[2,3\]. The next section will detail the selection of the antenna design.

# **3\. Design Methodology**

## **3.1 Key Antenna Performance Metrics**

Before diving into the antenna design selection, it is important to understand key antenna performance metrics.

**S11** is the ratio of the reflected voltage amplitude against the source voltage amplitude. It is a measure of how much the signal gets reflected due to impedance mismatches. For RF, the standard source impedance is 50 Ohms, so the antenna is also expected to be at 50 Ohms. The impedance bandwidth is the frequency range for which the S11 is \-10dB or less. Thus minimally from 13.92 to 13.98 GHz, the S11 must be \<-10dB. 

![][image2]

Fig. 2: S11 (dB) vs Frequency

**Polarisation** is the direction in which the vibrations of the electromagnetic wave is restricted. To lessen losses from polarisation mismatch, CubeSat antennae typically employ circular polarization (CP) \[1\].  Typically, **right-hand circular polarisation (RHCP)** is more commonly used for satellite communications, hence this was the chosen polarisation.

**Gain** describes how effectively the antenna concentrates radiated power in a particular direction compared to an isotropic radiator. A higher gain indicates a more focused beam. As mentioned, the peak gain will have to be \>=10dBi.

**Half-power beamwidth (HPBW)** is the angle between the points where the radiated power drops to half (−3 dB) of its peak value. It describes how wide or narrow the beam is. As mentioned, the half-power beamwidth must be at \+-12 degrees from the peak.

**Axial ratio (AR)** measures how circularly polarised the antenna is. A high axial ratio means the beam is elliptically polarized. When AR is very high, the beam is no different from linear polarization. AR \<3dB (2 times) is ideal.

## **3.2 Selection of antenna type** 

### **3.2.1 Concept evaluation matrix**

In various CubeSat antennae review papers, the most common types of planar antennae were patch antennae, followed by slot antennae and metasurface antennae \[1\]. A total of 4 factors were considered for selection of the best design:

1. Availability of formulae  
2. Simplicity of design for circular polarisation  
3. Space heritage  
4. Ease of manufacturing

The desired design is simple and suitable for a first-time antenna designer, as well as proven to work in existing space missions.

| Antenna type | Availability of design formulae | Simplicity of design for circular polarisation | Space heritage | Ease of manufacturing | Total |
| ----- | ----- | ----- | ----- | ----- | ----- |
| **Patch antenna** | 3 | 3 | 3 | 3 | 12 |
| **Slot antenna** | 2 | 1 | 1 | 2 | 6 |
| **Metasurface antenna** | 1 | 1 | 1 | 1 | 4 |

Table 1: Selection of antenna type

Using the evaluation matrix, patch antenna scores highest out of all factors considered and is hence chosen. This choice was also recommended early by both NUS and DSO mentors.  Circularly polarised patch antennas are extensively studied, with abundant formulae and well-validated design methods available in literature \[4\]. Patch antennae are also widely used in CubeSats \[1,2,3\] and can be easily manufactured via PCB manufacturing. 

In contrast, slot antennae and metasurface antennae are less commonly used in space systems, and achieving circular polarisation typically requires more complex geometries and heavier reliance on full-wave simulation \[5\]. Furthermore, for metasurface antennae, manufacturing can be complex as it requires intricate patterning.

Thus, **patch antenna** is still preferred as it scores highest across availability of design formulae, circular polarisation complexity, space heritage, and manufacturability.

### **3.2.2 Mitigating the Disadvantages of Patch Antenna**

**Limited Gain**: One patch antenna generally has small gain, but this can be mitigated as at high frequencies such as Ku-band, individual patch elements are small, enabling high-gain arrays without excessive footprint.

**Narrowband:** Patch antennas are narrowband due to their resonant nature. However, our mission’s bandwidth requirement is already narrow (e.g., ±0.03 GHz), thus this limitation is not critical.

### **3.2.3 About the Patch Antenna**

The patch antenna consists of a conducting patch layered on top of a dielectric substrate, which is on top of a conductive ground plane. Through a feedline, alternating E fields are formed between the patch and ground plane, which resonate and escape through both ends of the patch antenna which act as radiating slots. For a circular polarized patch antenna, the basic operating principle in which the E fields escape from the gaps between the patch and the ground plane is the same, but the geometry and feed points are changed to create circular polarisation.

 

Fig. 3: Rectangular Patch Antenna \[6\]

### **3.2.4. Preliminary feasibility calculations**

Utilising the formula for size of a rectangular patch antenna estimates that a singular Ku element would be of the size 7mm x 5.2mm \[7\]. One patch element can achieve around \~3-4dBi. 

To reach \>10dBi, we can double the element 3 times.

* 1 element: 3dBi  
* 2 elements: 6dBi  
* 4 elements: 9 dBi  
* 8 elements: 12 dBi

With a half wavelength (\~10.8mm) between each element, and considering a 2x4 array, the patches will only take up \~37mm by 18mm. \~0.3 wavelength extension on every side adds \~7mm of ground plane which gives 44mm by 21mm. Considering the required separation from metal, this is at least 6mm (half wavelength) from the mounting screws (Fig XX). Hence a microstrip patch array is a viable solution given our specifications.

## **3.3 Selection of type of patch antenna**

| ![][image3] | ![][image4] | ![][image5] |
| :---- | :---- | :---- |

Fig. 4: a) Truncated corner patch, b) Dual-feed patch with Wilkinson Power Divider, c) Circular patch

| Antenna Type | Gain | Simplicity of Design | Space Heritage | Total |
| ----- | ----- | ----- | ----- | ----- |
| **Truncated Square Patch (CP)**  | 1 | 3 | 2 | 6 |
| **Dual-Feed Rectangular Patch \+ Wilkinson Power Divider** | 3 | 1 | 3 | 7 |
| **Circular Probe-Fed Patch Array** | 3 | 2 | 3 | 8 |

Table 2: Selection of patch antenna design

Among the three designs considered, the truncated square patch was eliminated early due to its inherently lower gain \[8\], as highlighted by DSO mentors and supporting literature. The dual-feed rectangular patch can achieve good circular polarisation, but it requires a more complex feed structure per patch involving a Wilkinson power divider \[9\] and precise phase balancing. In contrast, the circular probe-fed patch achieves RHCP using a single feed to each patch, offering lower complexity while maintaining high gain and strong space heritage. This design is also supported by my NUS mentor. Therefore, the circular probe-fed patch antenna was selected.

## **3.4 Antenna Design Software**

Ansys HFSS is the primary software used due to the availability of tutorials online and the familiarity of my DSO mentor with it. CST Design Suite was also used initially as, unlike HFSS, it contains inbuilt formulae to calculate parameters of the circular patch array.

 

# **4\.  Prototype Development & Testing**

The prototypes discussed here are all antenna simulations in HFSS. Tests of key metrics mentioned prior are done after each simulation to evaluate the antenna performance. The key metrics are S11, Realized RHCP Gain, Beamwidth and Axial Ratio. Test results are discussed as well as steps for further improvement.

## **4.1 Prototype 1: Single Patch Simulation**

![][image6]![][image7]  
Fig. 5: a) Single patch in simulation, b) Circular patch parameters calculated by CST

By inputting frequency and dielectric constant, the diameter of patch Rp, side stub sizes and feed location Sf were calculated using the inbuilt formulae of CST Design Suite. This design was replicated on Ansys HFSS. 

![][image8]

Fig. 6: S11

The S11 is not tuned to our desired bandwidth of 13.95 \+- 0.03 GHz. Thus, Rp which affects the resonant frequency and Sf which affects the impedance seen at the feedpoint both have to be further tuned.

![][image9]

Fig. 7: Axial Ratio

The axial ratio is too high at 5 dB.

![][image10]

Fig. 8: Realised Gain

The antenna is left-hand-circular polarisation (LHCP) dominated instead of RHCP. Thus, the feedpoint needs to be ‘mirrored’. 

The gain is also unusually high for a single patch. It was later discovered that this was due to an error in the meshing frequency as it was not set at 13.95 GHz.

## **4.2 Prototype 2: 2x2 Array Simulation**

![][image11]

Fig. 9: 2x2 Array in simulation

The inbuilt formulae of CST had also suggested the separation between patches and the sequential rotation of patches for 2x2 array. Thus, replicating the patch created earlier, I simulated the 2x2 array.

![][image12]

Fig. 10: S11

The S11 was showing a spike at \~13.5 GHz, which is not acceptable. This was also likely an issue due to the meshing error.

![][image13]

Fig. 11: Axial Ratio

Axial ratio decreased from 5.6 to 1.8dB which is now acceptable. Compared to prototype 1, this shows that the sequentially rotated array has the effect of **decreasing axial ratio**.

![][image14]

Fig. 12: Realised Gain

As mentioned, the gain is still too high and it was due to the meshing error.

## **4.3 Prototype 3: Optimising single patch**

The main point of this prototype is to optimize the S11 for a single element. This helps create a good foundation for the overall S11 as there will be power reflections later on when the feed network is created for multiple patches. Also, the feedpoint is mirrored to produce RHCP instead of LHCP.  
![][image15]  
Fig. 13: S11  
Using parametric sweep, the best Rp and Sf parameters were found to produce a lowest possible S11 minimum of \-51 dB at 13.95 GHz. The optimal parameters were **Rp \= 3.092 mm, Sf \= 0.931mm.** Upon discussion with my DSO mentor, it was revealed that this patch is over-optimised, as it is not necessary to optimise the minimum beyond \-20dB.  
![][image16]  
Fig. 14: Realised Gain

The gain is now more reasonable at 4.5 dBi, and RHCP has been achieved  
![][image17]  
Fig. 15: Axial Ratio

A very high axial ratio of 14 dB is observed. However, it is theorised that putting the single patch into an array will minimise it, as seen earlier.

## **4.4 Prototype 4: Optimising 2x2 array**

![][image18]  
Fig. 16: 2x2 Array (Optimised)

This prototype takes the optimised single patch and forms a 2x2 array with it. The feeds will have to be excited at different phases to account for the physical rotations. From top left, clockwise: 0, 90, 180, 270 deg.  
![][image19]![][image20]  
Fig. 17: S11 optimisation (before vs after)

With the same Rp and Sf as the optimised patch, the S11 minimum is slightly shifted left of 13.95 GHz. Hence I decreased Rp and tuned Sf slightly to shift the minimum back to 13.95 GHz   
![][image21]  
Fig. 18: Realised Gain  
As expected, the gain reaches 10 dB. As the patch is doubled twice, an increase of 6dB from 4dB is expected.

![][image22]
Fig. 19: Axial Ratio  
Validating our theory, the sequential rotation has the effect of decreasing the axial ratio significantly from 14 to 0.9597 which is acceptable.

## **4.5 Prototype 5: Repositioning feed points**

Considering the location of the current feed points, possible feed networks were considered. A review of typical feed networks shows that typically, it consists of parts that can be duplicated (Fig. 20). Thus, it was thought that reversing the rotational pattern (Fig. 21\) to create regularly-spaced feed points would simplify the feed network. However, it was later realised that each feed to each feedpoint will need to have a slightly different length (¼ wavelength to account for a 90 degree phase shift), so the regularly-spaced feed points may not be necessary. Nonetheless, it later proved beneficial to investigate the effect of repositioning the feed points.  
![][image23]  
Fig. 20: Typical feed network  
![][image24]  
Fig. 21: Reversing rotational pattern (before vs after)

![][image25]  
Fig. 22: S11  
![][image26]  
Fig. 23: Axial Ratio  
![][image27]  
Fig. 24: Realised Gain  
The gain and S11 are similar to prototype 4\. However, the axial ratio actually decreased more from 0.96 to 0.0244 (only 1/5 of the previous) showing that this orientation is **very effective for minimising axial ratio**. 

## **4.6 Prototype 6: 2x4 Array Simulation**

From prototypes 4 and 5, the 2x2 arrays managed to achieve 10.7 dB and 10.2 dB respectively. This just meets our 10 dBi gain requirements. However, it is better to have a margin of 50% above 10 dB. Thus a safe gain value would be \~11.8 dBi. Hence, it was decided to double the 2x2 array to a 2x4 array, which theoretically increases gain from \~10 to \~13 dBi.  
![][image28]  
Fig. 23: 2x4 Array  
![][image29]  
Fig. 26: S11  
![][image30]  
Fig. 27: Realised Gain  
![][image31]  
Fig. 28: Axial Ratio  
The S11 is still \<-20dB within the required range. Now, the radiation pattern is no longer similar from all orientations as the array is rectangular instead of square. The narrowest beamwidth is taken at the Phi=90 deg cut. It still satisfies our HPBW requirements as gain is at \~9dB \> 7dB required at \+- 12 degrees from the peak. Noticeably, the axial ratio has increased from 0.024 to 0.6863. Thanks to prototype 5, the AR is optimally low.

## **4.7 Prototype 7: Feed network investigation**

![][image32]![][image33]

Fig. 29: a) Rectangular feed network (typical), b) Sequentially rotated ‘arc’ feed network

A quick prototype was created to investigate the type of feed network suitable to feed all patch elements. Generally, rectangular feed networks (Fig. 29a) are used due to their ease of design. However, for sequentially rotated arrays, a special arc feed network can be utilised (Fig. 29b), offering a simple means to add a fixed length for each phase shift, and minimising total feed length. The more complex arc feed network was investigated to see if it is viable. However, due to HFSS’s limited features for circular arc-creation, this proved cumbersome to create and hence it was rejected.  
![][image34]

Fig. 30: Attempt to draw arc feed network in HFSS

# **5\. Current Shortcomings ** 

| Shortcomings | Proposals |
| :---- | :---- |
| Loss of some earlier simulation drafts due to poor documentation | Better documentation from now on with labelling of HFSS files |
| In the later prototypes, I overlooked plotting the axial ratio at first (now included). | Test systematically from now. Always have a list of tests I must do for each prototype: gain, axial ratio, S11 |
| Could have done more investigation into parameters provided by CST:  presence of stubs patch spacing effect of sequential rotation vs no rotation 2x2 array | To include this in December plan |

Table 3: Shortcomings and Proposals to resolve them

# **6\. Detailed Project Completion Plan** 

| Date | Plan |
| :---- | :---- |
| 3-12 Dec | Investigate effect of CST-determined parameters: presence of stubs patch spacing effect of sequential rotation vs no rotation 2x2 array  Simulate repeated sections of feed network Simulate entire feed network (schematic version)  Layout feed network with patches and simulate |
| 14-21 Dec | Add in final SMA connector Make last adjustments and preparations required for manufacturing Send out design to PCB manufacturer by end of this week Make arrangements for antenna testing in W1 |
| W1 (11-16 Jan) |  Verify S11 with VNA  Full chamber measurements of antenna |
| W2–3 (18–31 Jan) | Compare measured S₁₁ and pattern vs simulation.• Identify discrepancy sources (substrate tolerance, connector mismatch, fabrication error) Re-simulate with measured substrate thickness and εᵣ. Tune model to align with measurements. |
| W4–5 (1–14 Feb) | Compare measured S₁₁ and pattern vs simulation. Identify discrepancy sources (substrate tolerance, connector mismatch, fabrication error). Re-simulate with measured substrate thickness and εᵣ. Tune model to align with measurements. |
| W6–Reading (17–28 Feb) | Submit revised PCB (if necessary). Conduct VNA \+ anechoic chamber retest. Document performance comparison between v1 and v2. |
| W7-8 (3–16 Mar) | Thermal and vibration tolerance study (simulation level unless you’re part of actual flight payload). Outgas-safe material review (Rogers datasheet, soldermask, adhesives). Write section on “space qualification considerations” for report. |
| W9 (17–23 Mar) | Interface study: SMA-to-coax routing inside satellite. Verify mechanical envelope fits 80 × 80 mm spec. Coordinate with bus team for mounting and RF chain (LNA, cables). |
| W10-11 (24 Mar – 6 Apr) | Compile design iterations, measurement results, lessons learned. Produce figures (S₁₁, AR, gain, radiation pattern comparisons). Write final report sections. |
| W12 (7–13 Apr) | Prepare slides & poster. Summarize key achievements: freq range 13.93–13.99 GHz, gain, axial ratio, fabrication results. |

 Table 4: Future Plans

 

# **7\. Conclusion** 

In conclusion, the antenna simulation work done in Semester 1 has paved a strong foundation for the design finalisation, followed by manufacturing and testing of the patch antenna array for next semester. Importantly, the 2x4 array was simulated, proving that the key metrics of S11, gain, beamwidth and axial ratio meet the mission and antenna requirements. In future, the lessons learnt from this semester will be applied to improve understanding of various parameters on the antenna performance, so as to create a more optimised design, adding the innovative edge to current research on Ku-band patch antennae. 

# **8\. References**

\[1\]  
Yusuf Salih Gurbet and Semih Doğu, “Comprehensive Review of Ku, K, and Ka Band Antenna Designs: Applications in CubeSats,” *International Journal of Aeronautical and Space Sciences*, Jun. 2025, doi: https://doi.org/10.1007/s42405-025-00989-5.  
\[2\]  
W. Silva, A. Campos, and J. Guerra, “A Compact Dual-Band UHF Microstrip Patch Antenna for CubeSat Applications,” *Journal of Communication and Information Systems*, vol. 36, no. 1, pp. 166–172, 2021, doi: https://doi.org/10.14209/jcis.2021.18.  
\[3\]  
K. B. Veera and K. D. Ajay, “Micro strip patch antenna utilization in cube satellite systems,” *i-manager’s Journal on Communication Engineering and Systems*, vol. 14, no. 1, p. 28, 2025, doi: https://doi.org/10.26634/jcs.14.1.21605.  
\[4\]  
C. A. Balanis, *Antenna theory analysis and design*. New York, N.Y. Wiley, 1997\.  
\[5\]  
Y. Amani and Y. ZEHFOROOSH, “Circularly Polarized Slot Antenna for wireless Applications,” *International Journal of Electronics, Mechanical and Mechatronics Engineering*, vol. 6, no. 3, pp. 1267–1274, Dec. 2016, doi: https://doi.org/10.17932/iau.ijemme.m.21460604.2016.6/3.1267-1274.  
\[6\]  
“Microstrip Patch Antenna,” *GeeksforGeeks*, Nov. 29, 2023\. https://www.geeksforgeeks.org/microstrip-patch-antenna/  
\[7\]  
“Microstrip Patch Antenna Calculator,” *Pasternack.com*, 2019\. https://www.pasternack.com/t-calculator-microstrip-ant.aspx  
\[8\]  
Zainal Muludi and Esmar Budi, “Truncated microstrip square patch array antenna 2 × 2 elements with circular polarization for S-band microwave frequency,” Sep. 2017, doi: https://doi.org/10.1109/elecsym.2017.8240384.  
\[9\]  
N. Richa, M. M. Sharma, I. B. Sharma, None Jaiverdhan, Priya Kaith, and J. Garg, “Design and Performance Evaluation of Circularly Polarized Dual Feed Microstrip Patch Antenna Using Wilkinson Power Divider,” *2021 IEEE Indian Conference on Antennas and Propagation (InCAP)*, pp. 12–14, Dec. 2021, doi: https://doi.org/10.1109/incap52216.2021.9726355.

**Acknowledgements**  
I would like to thank my DSO mentor Ms Huang Ying Ying and my NUS supervisor Mr Chua Tai Wei, both with extensive knowledge on antenna design, whose guidance without which I would not have been able to complete my design tasks this semester. I would also like to thank my NUS supervisor Mr Eugene Ee and Mr Ng Zhen Ning from Nuspace for the practical and valuable advice they have offered that help in the realisation of this project. 
[image1]: {{site.baseurl}}/Assets/images/fig/1.png
[image2]: {{site.baseurl}}/Assets/images/fig/2.png
[image3]: {{site.baseurl}}/Assets/images/fig/3.png
[image4]: {{site.baseurl}}/Assets/images/fig/4.png
[image5]: {{site.baseurl}}/Assets/images/fig/5.png
[image6]: {{site.baseurl}}/Assets/images/fig/6.png
[image7]: {{site.baseurl}}/Assets/images/fig/7.png
[image8]: {{site.baseurl}}/Assets/images/fig/8.png
[image9]: {{site.baseurl}}/Assets/images/fig/9.png
[image10]: {{site.baseurl}}/Assets/images/fig/10.png

[image11]: {{site.baseurl}}/Assets/images/fig/11.png
[image12]: {{site.baseurl}}/Assets/images/fig/12.png
[image13]: {{site.baseurl}}/Assets/images/fig/13.png
[image14]: {{site.baseurl}}/Assets/images/fig/14.png
[image15]: {{site.baseurl}}/Assets/images/fig/15.png
[image16]: {{site.baseurl}}/Assets/images/fig/16.png
[image17]: {{site.baseurl}}/Assets/images/fig/17.png
[image18]: {{site.baseurl}}/Assets/images/fig/18.png
[image19]: {{site.baseurl}}/Assets/images/fig/19.png
[image20]: {{site.baseurl}}/Assets/images/fig/20.png

[image21]: {{site.baseurl}}/Assets/images/fig/21.png
[image22]: {{site.baseurl}}/Assets/images/fig/22.png
[image23]: {{site.baseurl}}/Assets/images/fig/23.png
[image24]: {{site.baseurl}}/Assets/images/fig/24.png
[image25]: {{site.baseurl}}/Assets/images/fig/25.png
[image26]: {{site.baseurl}}/Assets/images/fig/26.png
[image27]: {{site.baseurl}}/Assets/images/fig/27.png
[image28]: {{site.baseurl}}/Assets/images/fig/28.png
[image29]: {{site.baseurl}}/Assets/images/fig/29.png
[image30]: {{site.baseurl}}/Assets/images/fig/30.png
