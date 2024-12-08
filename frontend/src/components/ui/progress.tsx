import React from 'react';

export const Progress: React.FC<{ value: number }> = ({ value }) => {
  return (
    <div className="w-full bg-gray-200 rounded-full h-2.5">
      <div
        className="bg-blue-600 h-2.5 rounded-full"
        style={{ width: `${value}%` }}
      />
    </div>
  );
};