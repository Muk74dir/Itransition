function longestCommonSubstring(...strings) {
    if (strings.length == 0) {
      return '';
    }
    let result = '';
    const firstString = strings[0];
  
    for (let i = 0; i < firstString.length; i++) {
      for (let j = i + 1; j <= firstString.length; j++) {
        const substring = firstString.slice(i, j);
  
        if (strings.every(str => str.includes(substring))) {
          if (substring.length > result.length) {
            result = substring;
          }
        }
      }
    }

    return result;
}

process.stdout.write(longestCommonSubstring(...process.argv.slice(2)) + '\n');
