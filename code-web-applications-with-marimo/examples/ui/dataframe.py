# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "vega-datasets==0.9.0",
# ]
# ///

import marimo

__generated_with = "0.10.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    from vega_datasets import data
    return (data,)


@app.cell
def _(data, mo):
    dataframe_transformer = mo.ui.dataframe(data.iris())
    dataframe_transformer
    return (dataframe_transformer,)


@app.cell
def _(dataframe_transformer):
    dataframe_transformer.value
    return


if __name__ == "__main__":
    app.run()
