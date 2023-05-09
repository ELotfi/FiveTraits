import os
import random
import json
import streamlit as st
st.set_page_config(layout="wide")


def display_history(history):
	hist = history.copy()
	for i in range(-2, -len(hist)-1, -2):
		hist[i] = f'-- **{hist[i]}**'
	return '  \n'.join(hist).lower()




def display_history_self(history):
	hist = history.copy()
	for i in range(-1, -len(hist)-1, -2):
		hist[i] = f'-- **{hist[i]}**'
	return '  \n'.join(hist)



def	add_sample(sample, vote):
		sample.update({"vote":vote})
		st.session_state.annotated.append(sample.copy())
		st.session_state.current_index += 1 



def annot_dialog():
	dial_col, gap_col1, annot_col1, gap_col2, annot_col2 = st.columns([.2,.1,1,.1,1])
	if dial_col.button("Save&Exit"):
		st.write(f"Saved.")
		return st.session_state.annotated
	else:
		if st.session_state.current_index < len(st.session_state.samples):
			sample = st.session_state.samples[st.session_state.current_index]
			dial_col.write(f"Sample {st.session_state.current_index + 1} out of {len(st.session_state.samples)}")
			#dial_col.caption("Persona:")
			#dial_col.write(sample['self_persona'])
			chats = sample['chats']
			trait = sample['trait']

			annot_col1.caption('Model1')
			annot_col1.write(display_history_self(chats['Model1']))
			annot_col2.caption(f'Model2')
			annot_col2.write(display_history_self(chats['Model2']))
			annot_col1.markdown("""---""")
			#annot_col2.markdown("""---""")
			vote = annot_col1.radio(f'Higher {trait}:', options=['Model1', 'Model2', 'Same'],index=0, horizontal=True)				
			annot_col1.button("Next", on_click=add_sample, args=(sample.copy(), vote))

		else:
			st.write(f"🎈 Done! All annotated.")
			return st.session_state.annotated




if __name__ == "__main__":
	data = json.load(open('data/samples_with_trait_dialog_both_100_sep.json'))
	if "annotated" not in st.session_state:
		st.session_state.annotated = []
		st.session_state.samples = data
		st.session_state.current_index = 0
	annotated = annot_dialog()
	json.dump(annotated, open(f'annotated_traits_dlg_both.json', 'w'))
	

#to do
# correct the yes/no labels
# collect and distribute qs from the same persona
# numbers