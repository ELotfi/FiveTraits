import os
import random
import json
import streamlit as st
import pandas as pd
#st.set_page_config(layout="wide")






def	add_sample(sample, vote):
		sample["votes"] = vote
		st.session_state.annotated.append(sample.to_dict().copy())
		st.session_state.current_index += 1 


def save_data(source_path, en):
	annotated = st.session_state.annotated
	current_idx = st.session_state.current_index
	results_path = f'results/annot_{source_path[5:-5]}_{en}_{en + current_idx}.json'
	json.dump(annotated, open(results_path, 'w'))
	json.dump({'st':en, 'en':en+current_idx}, open('results/last_session.json', 'w'))



def annot_persona(source_path, en):
	pers_col, gap_col1, annot_col = st.columns([1,.1,1])
	if pers_col.button("Save&Exit"):
		save_data(source_path, en)
		st.write(f"Saved.")
	else:
		if st.session_state.current_index < len(st.session_state.samples):
			sample = st.session_state.samples.loc[st.session_state.current_index]
			pers_col.write(f"Sample {st.session_state.current_index + 1} out of {len(st.session_state.samples)}")
			pers_col.caption("Persona:")
			persona = sample['persona'].split('.')
			persona = [p for p in persona if p !=""]
			pers_col.write(persona)
			#o,c,e,a,n = sample['Openness'],sample['Conscientiousness'],sample['Extraversion'], sample['Agreeableness'],sample['Neuroticism']

			vote_o = annot_col.radio('Openness', options=['probably high', 'probably low', 'no clues'], index=2, horizontal=True)
			annot_col.markdown("""---""")
			vote_c = annot_col.radio('Conscientiousness', options=['probably high', 'probably low', 'no clues'], index=2, horizontal=True)
			annot_col.markdown("""---""")
			vote_e = annot_col.radio('Extraversion', options=['probably high', 'probably low', 'no clues'], index=2, horizontal=True)
			annot_col.markdown("""---""")
			vote_a = annot_col.radio('Agreeableness', options=['probably high', 'probably low', 'no clues'], index=2, horizontal=True)
			annot_col.markdown("""---""")
			vote_n = annot_col.radio('Neuroticism', options=['probably high', 'probably low', 'no clues'], index=2, horizontal=True)	
			votes = {'Openness':vote_o,'Conscientiousness':vote_c, 'Extraversion':vote_e, 'Agreeableness':vote_a, 'Neuroticism':vote_n}
			annot_col.button("Next", on_click=add_sample, args=(sample.copy(), votes))			
			

		else:
			st.write(f"🎈 Done! All annotated.")




if __name__ == "__main__":
	source_path = 'data/persona_trait.csv'
	last_session =  json.load(open('results/last_session.json'))
	en = last_session['en']
	data = pd.read_csv(source_path)[en:]
	if "annotated" not in st.session_state:
		st.session_state.annotated = []
		st.session_state.samples = data
		st.session_state.current_index = 0

	annot_persona(source_path, en)

	

