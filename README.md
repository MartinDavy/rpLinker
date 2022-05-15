# rpLinker
generation of relationship graph between pc/npc of a role-playing campaign


## Compiling requirement

- python 3 (tested only on python 3.8)

- python lib graphviz
	- install with `pip install graphviz`

- Install graphviz on your computer:
	- For ubuntu with `sudo apt install graphviz`
	- For windows:
		- download it on this page https://www.graphviz.org/
		-  add the sub-directory in the `PATH` (cf https://www.computerhope.com/issues/ch000549.htm)

## Usage


```{python}
./rpLinker.py [DATA] [GRAPH NAME OUTPUT]
```

You can try this with the data given in the repository. You need to go to the root of this project and then use the following command:

```{python}
./src/rpLinker.py data/data.rpl example.png
```

You will obtain two files, *example.png* the image of the graph and *example.gv* graphviz file used to generate the image

## Description of the data format

*coming soon*