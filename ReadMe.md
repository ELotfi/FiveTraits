## 5 traits 
### Descriptions: 
![](img/traits_desc.png)
### Adjectives :
![](img/traits_adj.png)
![](img/traits.png)

## How to run:
- install streamlit: `pip install streamlit`
- There are 2 files in `data`: `trait_dialog_both.json` and `trait_dialog_self.json`. The idea is to do a trial on 10 samples from each (each sample has 5 pairs to be anotated!).
- You can specify the source file in `eval_trait.py`, line 63. You can start as it is and then change it to the other file.
- Running `streamlit run eval_trait.py` starts a server and opens a tab in your browser with the first sample: A pair of dialogs and a radio buttom to specify which one (Model1 or Model2) has the "higer" mentioned attribute (or it's the same).
- Clicking on `Next` after each annotation, shows the next pair. 5 of these pairs (each for a trait) complete 1 sample.
- At each point you can click on `Save&Exit` to save and exit. The results will be saved in the path mentioned in `eval_trait.py`, line 72. Next time that you run the code, it will start in the same (in line 63) from the place you left. 