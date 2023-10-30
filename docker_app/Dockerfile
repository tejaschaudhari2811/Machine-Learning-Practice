FROM continuumio/anaconda3:4.4.0
COPY . user/ML/app
EXPOSE 5000
WORKDIR /user/ML/app
RUN pip install -r requirements.txt
CMD python app.py

