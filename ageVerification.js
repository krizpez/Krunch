// Age verification module
const MINIMUM_AGE = 18;

function verifyAge(userAge) {
    if (userAge < MINIMUM_AGE) {
        throw new Error('You must be 18 years or older to use this application.');
    }
    return true;
}

module.exports = { verifyAge };