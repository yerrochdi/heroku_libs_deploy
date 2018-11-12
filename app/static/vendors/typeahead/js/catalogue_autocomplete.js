$(document).ready(function() {
  $.ajax({
    method: "GET",
    url: '/api/Catalogue/Libs/',
    success: function(data) {
      formationsLabels = data[0]
      addLibCat(formationsLabels)
    },
    error: function(error_data) {
      console.log("error")
      console.log(error_data)
    },
  })

  function addLibCat(libs) {
    var states = [ "TH CONN VALEURS GROUPE 1J",
        "PROVISOIRE ANGLAIS",
        "PROVISOIRE FRANCAIS",
        "PROVISOIRE ESPAGNOL",
        "GEN - FORMATION NEERLANDAIS",
        "GEN - FORMATION ITALIEN",
        "PROVISOIRE PORTUGAIS",
        "GEN - FORMATION ALLEMAND",
        "PROVISOIRE AUTRES LANGUES",
        "SSTH EXPLOITATION EP 3J",
        "SSTH FORAGE PUITS 3J",
        "ANGLAIS COURS INDIVIDUELS",
        "ANGLAIS COURS COLLECTIFS",
        "ANGLAIS IMMERSION",
        "ANGLAIS PARCOURS MIXTE",
        "ANGLAIS E-LEARNING TUTORE",
        "ALLEMAND COURS INDIVIDUELS",
        "ALLEMAND COURS COLLECTIFS",
        "ALLEMAND PARCOURS MIXTE",
        "ALILEMAND E-LEARNING TUTORE",
        "ESPAGNOL COURS COLLECTIFS",
        "PAU ESPAGNOL",
        "FRANCAIS COURS INDIVIDUELS",
        "FRANCAIS COURS COLLECTIFS",
        "FRANCAIS IMMERSION",
        "FRANCAIS COURSPART SPECIF",
        "ITALIEN E-LEARNING TUTORE",
        "NEERLANDAIS COURS INDIVIDUELS",
        "NEERLANDAIS COURS COLLECTIFS",
        "HONGROIS COURS INDIVIDUELS",
        "JAPONAIS COURS INDIVIDUELS",
        "ACCESS INITIATION",
        "ACCESS PERFECTIONNEMENT",
        "ACCESS MAITRISE",
        "ACCESS EXPERT",
        "ACROBAT INITIATION",
        "BO INITIATION",
        "BO PERFECTIONNEMENT",
        "BO EXPERT",
        "EXCEL INITIATION",
        "EXCEL PERFECTIONNEMENT",
        "EXCEL MAITRISE",
        "EXCEL EXPERT",
        "ILLUSTRATOR INITIATION",
        "ILLUSTRATOR PERFECTIONNEMENT",
        "INTERNET INITIATION",
        "PHOTOSHOP INITIATION",
        "PHOTOSHOP PERFECTIONNEMENT",
        "PHOTOSHOP MAITRISE",
        "POWERPOINT INITIATION",
        "POWERPOINT PERFECTIONNEMENT",
        "POWERPOINT MAITRISE",
];


    // constructs the suggestion engine
    var states = new Bloodhound({
      datumTokenizer: Bloodhound.tokenizers.whitespace,
      queryTokenizer: Bloodhound.tokenizers.whitespace,
      // `states` is an array of state names defined in "The Basics"
      local: libs
    });

    $('#bloodhound .typeahead').typeahead({
      hint: true,
      highlight: true,
      minLength: 1
    },
    {
      name: 'states',
      source: states
    });
  }
})
