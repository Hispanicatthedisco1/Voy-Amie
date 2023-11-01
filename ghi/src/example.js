

{
  comments.map((comments) => {
    return (
<div class="accordion" id="accordionExample" key={comments.comment_id}>
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button
        class="accordion-button collapsed"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#collapseTwo"
        aria-expanded="false"
        aria-controls="collapseTwo"
      >
        Accordion Item #2
      </button>
    </h2>
    <div
      id="collapseTwo"
      class="accordion-collapse collapse"
      data-bs-parent="#accordionExample"
    >
      <div class="accordion-body">
        <p>{comments.commenter}</p>
        <p>{comments.comment}</p>
      </div>
    </div>
  </div>
</div>;
    );
  });
}
