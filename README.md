# **Books_Recommendation_Platform**

---

### Naver BoostCamp AI Tech 5th Recsys Product Serving by Streamlit

> **Books_Recommendation_Platform**은 사용자 입력을 기반으로 책 추천을 제공하는 플랫폼입니다.  
> 머신 러닝 알고리즘을 사용하여 사용자의 입력 기반으로 어떤 책을 선호할지 예측합니다.
>
> Website - [**books-recommendation-platform**](https://brothergyu-books-recommendation-platform-book-recapp-d0pqn9.streamlit.app/)

<br>

## - Files

---

> ```markdown
> Books_Recommendation_Platform
> ├── Book_Rec
> │   ├── app.py
> │   ├── data
> │   │   ├── idx2info.pkl
> │   │   └── info2idx_convert_data.pkl
> │   ├── model
> │   │   ├── README.md
> │   │   ├── catboost_model_IALLC.pkl
> │   │   └── catboost_model_IALL_.pkl
> │   └── src
> │       ├── __init__.py
> │       ├── data_loader.py
> │       ├── info2idx.py
> │       ├── model_loader.py
> │       └── predict.py
> ├── README.md
> ├── poetry.lock
> └── pyproject.toml
> ```

이 프로젝트에는 다음과 같은 파일이 포함되어 있습니다:

### - app.py

> Streamlit 어플리케이션을 실행하는 주 파일입니다. 사용자 입력을 처리하고 결과로 나오는 책 추천을 표시합니다.
>
> 상위 book list를 하위 묘듈을 통해 반환을 받은 후 `info2idx.py`의 `info_data_load()`를 통해 books data를 불러온 후 request를 통해 책의 이미지를 불러오고 로컬 데이터셋에서 이름, 작가, 출판 년도를 합쳐 Streamlit 화면에 출력합니다

### - data 폴더

머신 러닝 모델에서 사용하는 데이터가 포함된 폴더입니다. `idx2info.pkl`과 `info2idx_convert_data.pkl` 두 개의 pickle 파일이 있습니다.

### - model 폴더

책 추천에 사용되는 머신 러닝 모델이 포함된 폴더입니다. `catboost_model_IALLC.pkl`과 `catboost_model_IALL_.pkl` 두 개의 pickle 파일이 있습니다.

### - src 폴더

머신 러닝 모델이 예측을 수행하는 데 사용하는 Python 모듈이 포함된 폴더입니다. `data_loader.py`, `info2idx.py`, `model_loader.py`, `predict.py`이 있습니다.

- data_loader.py

  >`idx2info.pkl`의 isbn의 값을 기반으로 add.py에서 받은 데이터를 합쳐 예측을 위한 인풋 데이터셋을 구성합니다

- info2idx.py

  > 에측을 위해서 `idx2info.pkl`, `info2idx_convert_data.pkl`의 파일을 불러와서` add.py`로 넘겨주는 파일입니다

- model_loader.py

  > `catboost_model_IALLC.pkl`, `catboost_model_IALL_.pkl` category 사용 여부에 따라 예측 모델을 `predict.py`로 넘겨주는 파일입니다
  
- predict.py

  > 인풋 데이터셋을 받아 예측 모델을 통해 rating을 예측하고 `app.py`로 결과를 반환합니다

### - README.md

현재 읽고 있는 파일입니다. 이 프로젝트의 개요와 사용 방법에 대한 설명을 제공합니다.

### - poetry.lock 및 pyproject.toml

이 파일들은 Poetry를 사용하여 프로젝트 종속성을 관리하는 데 사용됩니다.

<br>

## - Flow Chart

---

![image](https://user-images.githubusercontent.com/60868825/234962541-056c64c3-cefa-4108-a46c-0c3d92a4ade7.png)

<br>

## - Usage

---

책 추천 플랫폼을 사용하려면 다음 단계를 따르세요:

1. 이 저장소를 로컬 컴퓨터에 복제합니다.
2. Poetry를 사용하여 필요한 종속성을 설치합니다. `poetry install`
3. `app.py`를 실행합니다. `streamlit run app.py`
4. 웹 브라우저를 열고 `http://localhost:[할당된 포드번호]`로 이동합니다.
5. 데이터를 입력하고 "Recommend Books"를 클릭합니다.
6. 페이지에 표시되는 추천 책을 확인합니다.

<br>

## - License

---

- Python: PSF (Python Software Foundation) 라이선스
- CatBoost: Apache-2.0 라이선스
- Streamlit: Apache-2.0 라이선스
- Pandas: BSD-3-Clause 라이선스
- NumPy: BSD-3-Clause 라이선스