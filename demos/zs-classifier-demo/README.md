### Building a Simple Demo for Zero-Shot Classification

We built a demo for zero-shot classification using [Streamlit](https://streamlit.io/) which is great creating simple apps quickly.


Make sure you're currently in this demo directory:

`cd demos/zs-classifier-demo`

Run the demo

`make run`

To easily ship around the demo as a service, let's build a Docker container:

`make build`

This always takes a few minutes to complete. You can now run the container locally:

`docker run -p 9000:9000 -e --rm -it zs-classifier:0.1`
