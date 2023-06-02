"""Script renders README file based on ../metadata/DataList.xlsx"""

import pandas as pd
import copy

def csv_list_to_html(csv):
    """convert CSV list of variables to HTML list"""

    ## check to make sure csv is a string
    if type(csv)!=str:
        return csv

    ## Check there are commas
    elif ("," not in csv):
        return csv
        
    else:
        ## split list on commas and remove whitespace
        csv_list = csv.split(",")
        csv_list = [x.strip() for x in csv_list]
    
        ## put in HTML syntax
        prefix = "<ul> <li>"
        suffix = "</li> </ul>"
        middle = "</li> <li>".join(csv_list)
    
        return prefix + middle + suffix

def make_anchorlink(name):
    """Make anchor link for specified string"""

    ## make lowercase
    link_name = "-".join(name.lower().split())
    
    return f"[{name}](#{link_name})"

def print_category_table(data, category, cols_to_plot, file=None):
    """ Print comparison table for products in specific category. 
    'data' is a Pandas Dataframe.
    'category' is a string and cols_to_plot is a list of strings,
    corresponding to column names in the dataframe. """

    ## select subset of data with correct category and columns
    data_ = copy.deepcopy(data.loc[data["Category"]==category, cols_to_plot])

    ## sort by product and version
    data_ = data_.sort_values(by="Product and version")

    ## add anchor links to product and version
    prod_and_vers = data_["Product and version"]
    prod_and_vers = [make_anchorlink(x) for x in prod_and_vers]
    data_["Product and version"] = prod_and_vers
    
    print(f"# {category}\n", file=file)
    print(data_.to_markdown(index=False), file=file)

    return

def print_item_metadata(item, file=None):
    """Print out detailed metadata for single row of Pandas dataframe"""

    ## Make copy of item
    item_ = copy.deepcopy(item)
    
    ## Put variables in HTML list
    item_["Variables"] = csv_list_to_html(item_["Variables"])

    ## Add item with hyperlink to scripts
    path = f"scripts/{item_['Product and version']}" 
    item_["Download script"] = make_anchorlink(path)

    ## Remove row name
    item_ = item_.rename("")

    ## bold indices
    item_.index = pd.Index([f"**{i}**" for i in item_.index])

    print(f"### {item['Product and version']}", file=file)
    print(item_.to_markdown(), file=file)

    return

def main():
    """Main file: load data and print out metadata"""
    
    ## Load data
    data = pd.read_excel("../metadata/DataList.xlsx")
    
    ## unique categories (make new table for each one)
    cats = pd.unique(data["Category"])
    
    ## specify which columns to plot
    cols_to_plot = ["Product and version", "Spatial Resolution", "Temporal Resolution", "Period Available"]

    with open("../README.md", "w") as f:
    
        ### High-level comparison for categories
        for cat in cats:
            print_category_table(data, cat, cols_to_plot, file=f)
            print(f"\n\n", file=f)
        
        ### Detailed overview for each product
        for i, item in data.iterrows():
            print_item_metadata(item, file=f)
    return

if __name__ == "__main__":
    main()
