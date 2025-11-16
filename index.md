--- 
title: Intro
layout: home
nav_order: 1
---

<img src="Assets/images/intro/galassia_logo_final-inverse.png" alt="G5 logo" width="150">

# Galassia 5 Mission Overview <br>(CDE4301 Interim Report)

  
**1\. Galassia 5 Mission Overview**

### 1.1 Problem Statement

With the rapid expansion of Earth-observation CubeSats, current space-to-ground communication systems face two critical issues — data latency and spectrum congestion.  
 Existing missions rely heavily on post-processing of downlinked images and on X-band communication, which is increasingly saturated and requires large, expensive ground antennas. This limits real-time responsiveness in applications such as disaster monitoring or maritime surveillance.

To address these challenges, Galassia 5 is designed to demonstrate a new generation of AI-enabled, real-time Earth-observation capabilities supported by a Ku-band downlink system.  
 The mission aims to overcome traditional data-handling bottlenecks by performing on-orbit image processing and establishing direct high-speed downlinks to portable VSAT terminals.

### **1.2 Mission Objectives**

The primary objectives of the Galassia 5 mission are:

1. Demonstrate real-time imaging and onboard AI analytics using a Neural Processor Unit (NPU) integrated within the CubeSat.  
2. Validate a direct-to-VSAT Ku-band downlink for high-speed, low-latency data transfer between the satellite and portable ground stations.  
3. Showcase in-orbit reconfigurability, allowing the AI model and mission parameters to be updated remotely to support different operational scenarios.  
4. Evaluate thermal, mechanical, and electrical compatibility between the AI payload, radio unit, and the 6U satellite bus.

These goals collectively aim to advance Singapore’s capability in responsive, data-driven space operations.

### **1.3 Program Heritage**

![][image1]

The Galassia satellite program is an ongoing series of CubeSat missions by the National University of Singapore (NUS) aimed at advancing small satellite capabilities in science and technology.  
 The heritage of the program is as follows:

* **Galassia (2015):**  
   A 2U CubeSat (\~2 kg) launched for ionospheric observation and quantum entanglement experiments using the SPEQS payload.

* **Galassia 2 (2023):**  
   A 3U CubeSat (\~6 kg) carrying a multispectral agricultural Earth-sensing payload for precision imaging.

* **Galassia 5 (Planned 2027):**  
   A 6U CubeSat (\~12 kg) featuring *on-orbit AI image processing* and a *Ku-band radio payload*.  
   This mission represents a major leap toward real-time, intelligent Earth-observation and high-speed direct downlink capabilities.


  ### **1.4 Value Proposition**

  #### **1.4.1 Smart Earth Observations**

Onboard AI analytics extract only essential insights from captured imagery, drastically reducing redundant data and enabling faster decision-making.

#### **1.4.2 Accessibility and Spectrum Efficiency**

Operating in the **Ku-band** allows for smaller ground antennas and reduces reliance on congested X-band channels, enhancing portability for mobile or field users.

#### **1.4.3 Reconfigurability**

Galassia 5’s AI payload can be **reprogrammed in orbit**, adapting to evolving mission needs such as disaster monitoring, maritime surveillance, or environmental mapping.

### **1.5 Use Cases**

![][image2]

Galassia 5’s flexible payload design supports multiple real-world applications:

* **Humanitarian Rescue:** Rapid identification of collapsed infrastructure to assist first responders.

* **Forest Fire Surveillance:** Early detection of fire outbreaks and spread mapping.

* **Anti-Piracy Surveillance:** Continuous maritime monitoring for situational awareness over large oceanic regions.

These scenarios highlight the mission’s potential for **timely and actionable Earth-observation data**.

### **1.6 Concept of Operations (CONOPS)**

![][image3]

A representative **Anti-Piracy Surveillance** scenario operates as follows:

1. **Galassia 5** overflies a user vessel equipped with a Ku-band ground terminal.

2. The vessel transmits an *Area of Interest (AOI)* request to the satellite.

3. The satellite captures and processes imagery of the AOI.

4. The onboard AI identifies surrounding vessels and their positions.

5. The processed results are **downlinked directly** to the vessel via Ku-band.

This end-to-end workflow demonstrates real-time tasking, onboard intelligence, and immediate data return.

### **1.7 Payload System Architecture**

![][image4]

The **Payload Block Diagram** consists of the following core elements:

* **Payload Computer (PLC):** MPSoC-based single-board computer integrated with an AI accelerator (PCIe Gen 2 ×4).

* **Optical Imager:** Primary and backup sensors interfaced via SpaceWire, I²C, and USART links.

* **Payload Radio Unit (PRU):** Ku-band downlink transceiver and S-band uplink interface.

* **Bus Interfaces:** Electrical, mechanical, and data pathways connecting the payload to the satellite bus.

This modular layout ensures high-speed data throughput and robust fault tolerance for AI-driven imaging.

**1.8 Stakeholders and Collaborators**

**1.8.1 Institutional Stakeholders**

**![][image5]**

**1.8.2 University Partners**

![][image6]

### **1.9 Ku-Band Development Rationale and Motivation**

The Ku-band communication system for *Galassia 5* was developed under a mandate from MINDEF FSTD to explore operations in the Ku-band spectrum for small satellites.

#### Rationale for Ku-Band

Traditional X-band frequencies, while commonly used for Earth-observation downlinks are becoming increasingly congested and require large, high-gain antennas for effective reception.  
 Operating in the Ku-band offers several advantages for small-satellite missions:

* Enables smaller and more portable ground stations with equivalent signal gain.

* Reduces spectrum congestion by shifting away from heavily used X-band frequencies.

* Supports direct-to-VSAT communication, aligning with Galassia 5’s goal of real-time data delivery.

After consultation with IMDA, the Galassia 5 program received authorization to operate within the Earth-Exploration Service Downlink Band (13.93 – 13.99 GHz).  
 This dedicated frequency range lies outside standard Satcom bands, allowing the mission to achieve cost savings of approximately SGD 80,000 by avoiding international coordination fees while ensuring full regulatory compliance.

**![][image7]**

#### **Motivation and Technology Gap**

During feasibility studies, the team discovered that no existing commercial or space-qualified Ku-band communication hardware supported downlink operations within this specific frequency range.

Existing systems such as those from Kepler and ST Engineering operate within the 10.7–12.75 GHz band, which is incompatible with the *Galassia 5* allocated frequencies.  
 As a result, both the space payload (Ku-band radio) and the ground station had to be custom-engineered to meet the mission’s unique requirements.

This effort highlights the innovation-driven nature of the *Galassia 5* program, positioning it as a pioneering technology demonstrator for AI-assisted imaging and high-speed Ku-band communications in Singapore’s emerging space ecosystem.


[image1]: {{site.baseurl}}/Assets/images/intro/1.png
[image2]: {{site.baseurl}}/Assets/images/intro/2.png
[image3]: {{site.baseurl}}/Assets/images/intro/3.png
[image4]: {{site.baseurl}}/Assets/images/intro/4.png
[image5]: {{site.baseurl}}/Assets/images/intro/5.png
[image6]: {{site.baseurl}}/Assets/images/intro/6.png
[image7]: {{site.baseurl}}/Assets/images/intro/7.png