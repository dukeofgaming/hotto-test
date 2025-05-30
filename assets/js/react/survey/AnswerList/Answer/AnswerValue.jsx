import React from "react";
import TextAnswerValue from "./AnswerValue/TextAnswerValue";
import DateAnswerValue from "./AnswerValue/DateAnswerValue";
import BooleanAnswerValue from "./AnswerValue/BooleanAnswerValue";
import ObjectAnswerValue from "./AnswerValue/ObjectAnswerValue";
import ArrayAnswerValue from "./AnswerValue/ArrayAnswerValue";

const TYPE_COMPONENTS = {
  text: TextAnswerValue,
  date: DateAnswerValue,
  boolean: BooleanAnswerValue,
  object: ObjectAnswerValue,
  array: ArrayAnswerValue,
};

function AnswerValue({ type, value }) {
  const Component = TYPE_COMPONENTS[type];
  if (Component) {
    return <Component value={value} />;
  }
  console.log(
    `[AnswerValue] Unknown answer type encountered:`, type, value
  );
  return <span>{String(value)}</span>;
}

export default AnswerValue;
