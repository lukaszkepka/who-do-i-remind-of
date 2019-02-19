import React, { Component } from "react";

import NameForm from "./nameForm";
import DataBaseForm from "./databaseForm";
import PhotoForm from "./photoForm";
import ResultPage from "./resultPage";
import xService from "../services/appService";
import AllResults from "./resultRows";
import ErrorPage from "./errorPage";
import StepProgressBar from "./steps";
import Loader from "./loader";

import "./app.scss";

const initialState = {
  userName: "",
  userPhoto: null,
  dataBase: null,
  isDataBaseSet: false,
  isLoading: false,
  hasError: false,
  similarPeople: [],
  shouldShowAllResults: false
};

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {...initialState, dataBases: []};

    this.service = new xService();

    this.handleNameChange = this.handleNameChange.bind(this);
    this.handleDataBaseChange = this.handleDataBaseChange.bind(this);
    this.handlePhotoChange = this.handlePhotoChange.bind(this);
    this.handleResetClicked = this.handleResetClicked.bind(this);
    this.showAllResults = this.showAllResults.bind(this);
    this.hideAllResults = this.hideAllResults.bind(this);
    this.resetUserPhoto = this.resetUserPhoto.bind(this);
  }

  componentDidMount() {
    this.service
      .getDataBases()
      .then(response =>
        this.setState({ dataBases: response, dataBase: response[0] })
      );
  }

  handleNameChange(userName) {
    this.setState({ userName });
  }

  handleDataBaseChange(baseId) {
    this.setState({ dataBase: baseId, isDataBaseSet: true });
  }

  handlePhotoChange(userPhoto) {
    this.setState({ userPhoto, isLoading: true });
    this.service
      .getSimilarPeople(userPhoto, this.state.dataBase)
      .then(response =>
        this.setState({
          similarPeople: response,
          isLoading: false,
          hasError: false
        })
      )
      .catch(err => {
        console.log("xD");
        this.setState({
          isLoading: false,
          hasError: true,
          userPhoto: null
        });
      });
  }

  resetUserPhoto() {
    this.setState({ hasError: false, userPhoto: null });
  }

  handleResetClicked() {
    this.setState(initialState);
  }

  showAllResults() {
    this.setState({ shouldShowAllResults: true });
  }

  hideAllResults() {
    this.setState({ shouldShowAllResults: false });
  }

  render() {
    console.log(this.state);
    const {
      dataBases,
      userName,
      dataBase,
      isDataBaseSet,
      userPhoto,
      isLoading,
      similarPeople,
      shouldShowAllResults,
      hasError
    } = this.state;

    let content = null;
    if (!dataBases.length) {
      content = (
        <>
          <h1 className="title">Who do I remind of?</h1>
          <Loader />
        </>
      );
    } else if (!userName) {
      content = (
        <>
          <h1 className="title">Who do I remind of?</h1>
          <StepProgressBar currentStep={0} />
          <NameForm onNameSubmit={this.handleNameChange} />
        </>
      );
    } else if (!isDataBaseSet) {
      content = (
        <>
          <h1 className="title">Who do I remind of?</h1>
          <StepProgressBar currentStep={1} />
          <DataBaseForm
            dataBases={dataBases}
            onDataBaseSubmit={this.handleDataBaseChange}
          />
        </>
      );
    } else if (!userPhoto) {
      content = (
        <>
          <h1 className="title">Who do I remind of?</h1>
          <StepProgressBar currentStep={2} />
          <PhotoForm onPhotoSubmit={this.handlePhotoChange}>
            {hasError && <ErrorPage />}
          </PhotoForm>
        </>
      );
    } else if (isLoading) {
      content = (
        <>
          <h1 className="title">Who do I remind of?</h1>
          <Loader />
        </>
      );
    } else if (userName && userPhoto && !isLoading && !shouldShowAllResults) {
      content = (
        <>
          <h1 className="title">Who do I remind of?</h1>
          <ResultPage
            userPhoto={URL.createObjectURL(userPhoto)}
            userName={userName}
            similarPeople={similarPeople}
            onResetClick={this.handleResetClicked}
            onShowAllResultsClick={this.showAllResults}
          />
        </>
      );
    } else if (shouldShowAllResults) {
      content = (
        <>
          <h1 className="title">Who do I remind of?</h1>
          <AllResults
            onResetClick={this.handleResetClicked}
            onBackClick={this.hideAllResults}
          />
        </>
      );
    } else {
      console.log(this.state);
      console.log("NIGDY NIE POWINIENEM TU WEJŚĆ");
      content = "NIGDY NIE POWINIENEM TU WEJŚĆ";
    }

    return <div className="app">{content}</div>;
  }
}
