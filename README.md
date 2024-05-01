## A website for user research findings

**HTML Files**

- `index.html`:
    - Static page that provides a brief description of the website's purpose and a button to proceed to the findings page.
- `findings.html`:
    - Dynamic page that displays the user research findings. It will have a placeholder area where Flask will inject the findings data.

**Routes**

- `/`:
    - Route for the index page. It will render the `index.html` file.
- `/findings`:
    - Route for the findings page. It will render the `findings.html` file and pass the user research findings as a variable to the template. This data can be retrieved from a database or a data file.