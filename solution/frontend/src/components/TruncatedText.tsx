import React from 'react';

interface TruncatedTextProps {
  text: string | null;
  maxLength: number;
}

const TruncatedText: React.FC<TruncatedTextProps> = ({ text, maxLength }) => {
  if ( text == null) {
    return "";
  } else {
    const truncated = text.length > maxLength ? text.slice(0, maxLength) + '...' : text;

    return <span>{truncated}</span>;
  }
  
};

export default TruncatedText;