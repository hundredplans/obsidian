Specifics how a specific element should be displayed
```css
h1, p1, em { /* Reference multiple */
	color: forestgreen;
	font-size: larger;
	font-family: sans-serif, Courier;
}

h1 em { /* All ems inside h1's are blue */
	color: blue;
}

#id { /* Reference by id */

}

.class { /* Reference by class, <li class="whatev">*/

}
```

If font-family not found it falls back on the next one in the list

```css
div {
	width: 20vw;
	height: 20vw;
}
```

```css
h1 em 
h1 > em
h1 + em
h1 ~ em
```
" " - Inside the tag, not directly inside
\> - Directly inside
\+ - Directly after
~ - All specified elements after specificed element

```css
h1 {} [0] [0] [1] /* References by index */
h1.class_one.class_two
```