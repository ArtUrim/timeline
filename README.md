# Timeline

drawing project timeline (Gantt as well as in a calendar).

## PNG generation

### CLI

`# wkhtmltoimage file:///home/artur/Test/python/timeline/cal.html cal.png`

`# wkhtmltoimage --width 724  file:///home/artur/Test/python/timeline/cal.html cal.png`

### python

Install

`# pip install imgkit pdfkit`

`# sudo apt-get install wkhtmltopdf`

python

`>>> import imgkit`

`>>> imgkit.from_url('https://example.com', 'output.png')`
