// create a function that removes the first and last characters of a string.

const removeChar = str => {
    let newStr = ''
    for(let i=0; i<str.length; i++){
      if(i !== 0 && i !== str.length -1){
        newStr += str[i]
      }
    }
    return newStr
  }
  