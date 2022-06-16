### Demo

This demo is implemented with [Streamlit](https://streamlit.io/) which is great for creating simple demo apps quickly.


Make sure you're currently in this demo directory:

`cd demos/first-demo`


Create a new environment for the demo (optional but recommended if the demo becomes complex!)

```
conda create -n <env-name> python=3.8 # if using Anaconda, or use your preferred method
conda activate <env-name>
```

Install demo requirements

`make dev`

Run the demo

`make run`

To easily ship around the demo as a service, let's build a Docker container:

`make build`

This always takes a few minutes to complete. You can now run the container locally:

`docker run -p 8000:8000 -e --rm -it PKG_NAME-demo:0.1`
