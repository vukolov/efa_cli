# Events Flow Analyser Configuration Client
The part of https://github.com/vukolov/events_flow_analyser

## Overview
The **Events Flow Analyser Configuration Client** is a microservice designed to handle the configuration of the Events Flow Analyser.

## Features
You can use it for:
* Adding and configure new data sources
* Adding and configure new metrics
* Adding new metric groups and joining metrics to them
* Set up the access policy for the data visualyzer (Grafana, etc.)

## Requirements
python 3.11 or higher

## Commands
```efa-cli login```

```efa-cli metrics add <metric-name>```

```efa-cli metrics lst --name <metric-name>```