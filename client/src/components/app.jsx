import React, { Component } from "react";
import AnimateHeight from "react-animate-height";

import NameForm from "./nameForm";
import PhotoForm from "./photoForm";
import ResultPage from "./resultPage";
import xService from "../services/xService";
import AllResults from "./resultRow";
import ErrorPage from "./errorPage";

import "./app.scss";

const initialState = {
  userName: "",
  userPhoto: null,
  isLoading: false,
  hasError: false,
  similarPeople: [],
  shouldShowAllResults: false
};

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = initialState;

    this.service = new xService();

    this.handleNameChange = this.handleNameChange.bind(this);
    this.handlePhotoChange = this.handlePhotoChange.bind(this);
    this.handleResetClicked = this.handleResetClicked.bind(this);
    this.showAllResults = this.showAllResults.bind(this);
    this.hideAllResults = this.hideAllResults.bind(this);
    this.resetUserPhoto = this.resetUserPhoto.bind(this);
  }

  handleNameChange(userName) {
    this.setState({ userName });
  }

  handlePhotoChange(userPhoto) {
    this.setState({ userPhoto, isLoading: true });
    this.service
      .getSimilarPeople(userPhoto)
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
          hasError: true
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
      userName,
      userPhoto,
      isLoading,
      similarPeople,
      shouldShowAllResults,
      hasError
    } = this.state;

    let content = null;
    if (!userName) {
      content = (
        <>
          <h1 className="title">Who do I remind of?</h1>
          <NameForm onNameSubmit={this.handleNameChange} />
        </>
      );
    } else if (!userPhoto) {
      content = (
        <>
          <h1 className="title">Who do I remind of?</h1>
          <PhotoForm onPhotoSubmit={this.handlePhotoChange} />
        </>
      );
    } else if (isLoading) {
      content = <div>Loading...</div>;
    } else if (hasError) {
      content = <ErrorPage onOkClick={this.resetUserPhoto} />;
    } else if (userName && userPhoto && !isLoading && !shouldShowAllResults) {
      content = (
        <ResultPage
          userPhoto={URL.createObjectURL(userPhoto)}
          userName={userName}
          similarPeople={similarPeople}
          onResetClick={this.handleResetClicked}
          onShowAllResultsClick={this.showAllResults}
        />
      );
    } else if (shouldShowAllResults) {
      content = (
        <AllResults
          onResetClick={this.handleResetClicked}
          onBackClick={this.hideAllResults}
        />
      );
    }

    return (
      <div className="app">
        <AnimateHeight duration={500} height={"auto"}>
          {content}
        </AnimateHeight>
      </div>
    );
  }
}
