$(function(){
    $('.vote').on('click', function(){
        var pk = $(this).attr('id');
        console.log(pk)
        $.ajax({
            url: `/vote/${pk}/`,
            type: 'GET'
        })
        .done((data)=>{
            var votesElement = `#votes-${pk}`
            var votes = Number($(votesElement).text());
            votes += 1;
            $(votesElement).text(votes);
        })
        .fail((data)=>{
            console.log('fail')
        })
    });
    $('button#add').on('click', function(){
        var totalChoices = $('input#id_choice_set-TOTAL_FORMS');
        var maxChoiceNum = 10;
        var currentChoiceNum = parseInt(totalChoices.val());
        if (Number(currentChoiceNum) == maxChoiceNum) {
            $(this).after('<span>Up to 10</span>');
            totalChoices.attr('value', maxChoiceNum + 1);
            return
        } else if (Number(currentChoiceNum) >= 11) {
            return
        }
        var choiceId = 'id_choice_set-' + currentChoiceNum + '-text'

        var labelElement = $('<label>Text:\u00a0</label>', {for: choiceId});
        var textElement = $('<input>', {
            type: 'text',
            id: choiceId,
            max_length: '200',
            name: 'choice_set-' + currentChoiceNum + '-text'
        });
        var choiceElement = $('<p>', {id: choiceId})

        choiceElement.append(labelElement);
        choiceElement.append(textElement);
        $('div.choice').append(choiceElement);

        currentChoiceNum += 1;
        totalChoices.attr('value', currentChoiceNum);
    });
});
