# Html table to csv converter

Read all files (valid html pages containing a table) in `/data/in/files/**/*` (regarldess of extensions and how deeply they are nested), parse with [pd.read_html](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_html.html) and write to corresponding locations in `/data/out/files`

I dont actually think anyone else will reuse this, but here's our usecase

We are receiving a file which have `.xls` extension, but upon detailed inspection it's actualy a `html` table. [Existing xlsx processor](https://github.com/jakubbartel/keboola-xls2csv-processor) can't read it as excel so we have to use `pd.read_html()`

It's built on top of the huge keboola custom science python image, because installing the compilers, lxml and stuff on alpine is pain + it needs to be recompiled on each CI build.

# Configuration
```
{
    "definition": {
        "component": "pocin.processor-html2csv"
    }
}


```

## Run locally

```

docker-compose run --rm dev
```

## Run tests
	

```
make test
# after dev session is finished to clean up containers..
make clean 
```
