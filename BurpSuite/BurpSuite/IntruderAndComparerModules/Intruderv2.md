## Sniper

- Sniper uses a single set of payload.
- It enumerates one parameter at a time.
- For multiple parameters, it takes each in turn and enumerates with each payload from the supplied list that we upload.

** If there are ten payloads with two parameters, it will make as 20 requests.**

## Battering Ram

- It uses a single set of payload.
- It enumerates all parameter in a single request using the same payload.

** This will make only ten requests since it is using both the parameter in a single request as the same payload. **

## Pitchfork
- Pitchfork uses multiple payload sets.
- It enumerates all parameters in a single request.
- But using a separate payload for each parameter.
- Process ends with the length of the smallest payloads set.

**It will use the respective payload from both word-lists.**

## Cluster Bomb

- Cluster bomb uses multiple payload sets.
- It enumerates over multiple parameters by using all the possible combination payload from multiple requests' provided word-lists.

**It will make all the possible combination of both the list. So around 25 possible combinations will appear. The length of the value will be changed for the responding payloads.
**
