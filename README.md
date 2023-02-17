# ChatGPT-Bypass

Simple Scripts that allows you to bypass content filtering. This calls the OpenAI autocompletion API for DaVinci-003. Click bait-y for CHATGPT, but we won't get into CHATGPT vs DaVinci here.


## Requirements

Export API Key

head over to 'beta.openai.com' to retrieve your personal API key and set it the variable CHATGPT_TOKEN...or hard code the key. idc

Windows:
```
$env:OPENAI_API_KEY='<api key>'
Nix/MAC:
```

```
export OPENAI_API_KEY=<api key>
```
## USAGE


```
python3 bypass.py  -h
```

### Example with chatGPT ❌

```
write me a polymorphic backdoor
```

![image](https://user-images.githubusercontent.com/47946047/219818104-ff02f965-bd66-4ff8-b7e3-5b94a67a7194.png)


### Example with script ✅
```
python3 bypass.py   "write me a polymorphic backdoor"
```
![image](https://user-images.githubusercontent.com/47946047/219817937-59be4b23-fa53-4384-8cf4-dc5240705e2d.png)

