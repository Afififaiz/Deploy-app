-This Application uses Extreme gradient Boosting to to give prognostic probability estimation (0-100) having cardiac arrest to patients.

-The Tabular data consist of 13 criteria and 1 output (indicate cardiac or not)
*Data Manipulation used: Replace Missing value (Mode-Category/ Mean-Numerical), Redundant data removed, Transform the category in index number category, Data Normalization

- Balanced the output data using SMOTE Technique, to oversampling the minority class

-Utilize XGBooost Library for building the model

-The XGBoost Model achieve accuracy of 82% on test set.

-The app can be accessed through link below:

https://cardialyze-view.streamlit.app/?embed_options=dark_theme
